#import select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.select import Select
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#wait = WebDriverWait(driver, timeout=60)
import time

def test():
    driver.get("https://www.nahla.ba")
    title = driver.title
    print(title)
    ime_newsletter = driver.find_element(By.ID,"mce-FNAME")
    ime_newsletter.click()
    ime_newsletter.clear()
    ime_newsletter.send_keys("almir")
    time.sleep(10)
    driver.quit()

test()