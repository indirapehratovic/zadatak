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
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    

    def artikli(self):
        dodaj_artikal1 = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        dodaj_artikal1.click()
        dodaj_artikal2 = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        dodaj_artikal2.click()
        ikona_kosara = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        ikona_kosara.click()
        kosara = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(kosara.text)
        assert kosara.text == "YOUR CART"
        time.sleep(1) #provjeriti dok se ne ucita stranica
        sadrzaj_kosare = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        #print(sadrzaj_kosare[0].text)
        #print(sadrzaj_kosare[1].text)
        assert len(sadrzaj_kosare) == 2
        assert sadrzaj_kosare[0].text == "Sauce Labs Onesie"
        assert sadrzaj_kosare[1].text == "Sauce Labs Bike Light"
        izlaz = self.driver.find_element(By.ID, "checkout")
        print(izlaz.text)
        izlaz.click()
        provjera_izlaz = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(provjera_izlaz.text)
        assert provjera_izlaz.text == "CHECKOUT: YOUR INFORMATION"
        firstname_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        firstname_polje.clear()
        firstname_polje.click()
        firstname_polje.send_keys("Indira")
        lastname_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        lastname_polje.clear()
        lastname_polje.click()
        lastname_polje.send_keys("Pehratovic")
        postalcode_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        postalcode_polje.clear()
        postalcode_polje.click()
        postalcode_polje.send_keys("71000")
        time.sleep(1)
        nastavi = self.driver.find_element(By.ID, "continue")
        nastavi.click()
        time.sleep(1)
        provjera_pregled = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(provjera_pregled.text)
        assert provjera_pregled.text == "CHECKOUT: OVERVIEW"
        sadrzaj_pregleda = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        print(sadrzaj_pregleda[0].text)
        print(sadrzaj_pregleda[1].text)
        assert len(sadrzaj_pregleda) == 2
        assert sadrzaj_pregleda[0].text == "Sauce Labs Onesie"
        assert sadrzaj_pregleda[1].text == "Sauce Labs Bike Light"
        time.sleep(1)
        kraj = self.driver.find_element(By.ID, "finish")
        kraj.click()
        provjera_complete = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        print(provjera_complete.text)
        assert provjera_complete.text == "CHECKOUT: COMPLETE!"
        time.sleep(1)
        ikona_izbornik = self.driver.find_element(By.ID, "react-burger-menu-btn")
        ikona_izbornik.click()
        time.sleep(1)
        logout_link = self.wait.until(EC.visibility_of_element_located ((By.ID,"logout_sidebar_link")))
        logout_link.click()
        time.sleep(1)
        provjera_login = self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        #print(provjera_login.value)
        #assert provjera_login.text == "Login"

    def get_text(self):
        products_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return products_element.text
   
     
    
    
    #def get_alert_text(self):
        #alert_prozor = self.wait.until(EC.alert_is_present())
        #return alert_prozor.text