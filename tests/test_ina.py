from pages.sauce_page import SaucePage

def test_login(driver):
    sauce_page = SaucePage(driver)
    sauce_page.go_to("https://www.saucedemo.com")
    sauce_page.login("standard_user", "secret_sauce")
    assert sauce_page.get_text() == "PRODUCTS"
    sauce_page.artikli()
    
  

#def test_incorrect_login(driver):
    #home_page = HomePage(driver)
    #home_page.go_to("https://www.demoblaze.com")
    #home_page.login("admin_ahmet", "admin")
    #assert home_page.get_alert_text() == "User does not exist"