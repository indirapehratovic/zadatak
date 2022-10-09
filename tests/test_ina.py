from pages.sauce_demo import SauceDemo

def test_login(driver):
    sauce_demo = SauceDemo(driver)
    sauce_demo.open()
    sauce_demo.login_page()
    sauce_demo.articles_page()
    sauce_demo.basket_page()
    sauce_demo.checkout_information_page()
    sauce_demo.overview_page()
    sauce_demo.logout_page()
  
