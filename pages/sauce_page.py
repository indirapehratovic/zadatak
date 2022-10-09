from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class SaucePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username, password):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.click()
        username_field.send_keys(username)
        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.click()
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    

    def articles(self):
        add_article1_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        add_article1_button.click()
        add_article2_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_article2_button.click()
        basket_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        basket_icon.click()
        basket_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(basket_title.text)
        assert basket_title.text == "YOUR CART"
        time.sleep(1) #provjeriti dok se ne ucita stranica
        basket_content = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        #print(sadrzaj_kosare[0].text)
        #print(sadrzaj_kosare[1].text)
        assert len(basket_content) == 2
        assert basket_content[0].text == "Sauce Labs Onesie"
        assert basket_content[1].text == "Sauce Labs Bike Light"
        checkout_button = self.driver.find_element(By.ID, "checkout")
        print(checkout_button.text)
        checkout_button.click()
        checkout_information_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(checkout_information_title.text)
        assert checkout_information_title.text == "CHECKOUT: YOUR INFORMATION"
        firstname_field = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        firstname_field.clear()
        firstname_field.click()
        firstname_field.send_keys("Indira")
        lastname_field = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        lastname_field.clear()
        lastname_field.click()
        lastname_field.send_keys("Pehratovic")
        postalcode_field = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        postalcode_field.clear()
        postalcode_field.click()
        postalcode_field.send_keys("71000")
        time.sleep(1)
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        time.sleep(1)
        overview_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(overview_title.text)
        assert overview_title.text == "CHECKOUT: OVERVIEW"
        inventory_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        print(inventory_items[0].text)
        print(inventory_items[1].text)
        assert len(inventory_items) == 2
        assert inventory_items[0].text == "Sauce Labs Onesie"
        assert inventory_items[1].text == "Sauce Labs Bike Light"
        time.sleep(1)
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
        checkout_complete_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(checkout_complete_title.text)
        assert checkout_complete_title.text == "CHECKOUT: COMPLETE!"
        time.sleep(1)
        menu_icon = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_icon.click()
        time.sleep(1)
        logout_link = self.wait.until(EC.visibility_of_element_located ((By.ID,"logout_sidebar_link")))
        logout_link.click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        

    def get_text(self):
        products_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return products_element.text
   
     
    
    
    #def get_alert_text(self):
        #alert_prozor = self.wait.until(EC.alert_is_present())
        #return alert_prozor.text