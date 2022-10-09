from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username, password):
        login_link = self.wait.until(EC.element_to_be_clickable((By.ID, "login2")))
        login_link.click()
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "loginusername")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "loginpassword")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//button[text()='Log in']")
        login_button.click()
    
    def get_welcome_text(self):
        welcome_element = self.wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        return welcome_element.text
    
    def get_alert_text(self):
        alert_prozor = self.wait.until(EC.alert_is_present())
        return alert_prozor.text