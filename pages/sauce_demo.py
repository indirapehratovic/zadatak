from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class SauceDemo:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def open(self):
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
    
    def login_page(self):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.click()
        username_field.send_keys("standard_user")
        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.click()
        password_field.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def assert_title(self, expected_title):
        header_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        assert header_title.text == expected_title

    def assert_cart_items(self, items):
        assert len(items) == 2
        assert items[0].text == "Sauce Labs Onesie"
        assert items[1].text == "Sauce Labs Bike Light"


    def articles_page(self):
        self.assert_title("PRODUCTS")
        add_article1_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        add_article1_button.click()
        add_article2_button = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_article2_button.click()
        basket_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        basket_icon.click()


    def basket_page(self):
        self.assert_title("YOUR CART")
        basket_content = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assert_cart_items(basket_content)
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

    def checkout_information_page(self):  
        self.assert_title("CHECKOUT: YOUR INFORMATION")
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
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()

    def overview_page(self):
        self.assert_title("CHECKOUT: OVERVIEW")
        inventory_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.assert_cart_items(inventory_items) 
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

    def logout_page(self):
        self.assert_title("CHECKOUT: COMPLETE!")
        menu_icon = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_icon.click()
        logout_link = self.wait.until(EC.visibility_of_element_located ((By.ID,"logout_sidebar_link")))
        logout_link.click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        

    
   
     
    