import time

from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen
from selenium.webdriver.support import expected_conditions as EC



class Test_001_login_page:
    baseURL = ReadConfig.get_baseURL()
    loginURL = ReadConfig.get_loginURL()
    password = ReadConfig.get_password()
    email = ReadConfig.get_email()
    logger = LogGen.loggen()  # -> logger object will return logger object from Loggen method created at utilis.

    # def test_home_page_title(self, setup):
    #     self.logger.info("****Test_001_login_page****")
    #     self.logger.info("****Verify home page title****")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     actual_title = self.driver.title
    #     if actual_title == "Home Page":
    #         assert True
    #         self.driver.close()
    #         self.logger.info("**Home page title verified**")
    #
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
    #         self.driver.close()
    #         self.logger.error("***Login test is failed**")
    #         assert False

    def test_login(self, setup):
        self.logger.info("****test_login****")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_sign_in()
        self.lp.click_customer_toggle_menu()
        time.sleep(5)
        self.lp.click_logout()
        time.sleep(5)

