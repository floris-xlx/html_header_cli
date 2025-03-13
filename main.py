from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import os
import time

def fetch_html_head(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    try:
        print("URL:", url)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(executable_path='./chromedriver.exe')  
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        
        # Wait for 2 seconds to ensure everything is loaded
        time.sleep(2)
        
        head = driver.find_element(By.TAG_NAME, 'head')
        if head:
            html_head = head.get_attribute('outerHTML')
            print("HTML Head:")
            print(html_head)
            
            # Create 'sites' directory if it doesn't exist
            if not os.path.exists('sites'):
                os.makedirs('sites')
            
            # Save the HTML head to a text file named after the URL
            filename = os.path.join('sites', url.replace("https://", "").replace("http://", "").replace("/", "_") + '.txt')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(html_head)
        else:
            print("No HTML head found.")
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        fetch_html_head(sys.argv[1])
