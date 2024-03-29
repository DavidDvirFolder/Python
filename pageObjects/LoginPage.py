from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    # Locators:
    button_signIn_css = "fieldset[class='fieldset login'] div[class='primary'] span"
    link_sign_in_grid_xpath = "//div[@class='panel header']//ul[@class='header links']"
    link_sing_in_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"
    textbox_email_css = "input#email"
    textbox_password_css = "fieldset.fieldset input#pass"
    # click the button to open sign out link
    button_customer_menu_css = "div[class='panel header'] button[type='button']"
    # click the logout button
    link_signOut_xpath = "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']"
    text_welcome_message_xpath = "(//span[@class='logged-in' and text()='Welcome, George Biden!'])[1]"

    # Action methods for the locators,
    # and initialize the constructor

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        email_element = self.driver.find_element(By.CSS_SELECTOR, self.textbox_email_css)
        email_element.clear()
        email_element.send_keys(email)

    def set_password(self, password):
        password_element = self.driver.find_element(By.CSS_SELECTOR, self.textbox_password_css)
        password_element.clear()
        password_element.send_keys(password)

    def click_sign_in_link(self):
        # Wait for the "Sign In" link to be clickable
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.link_sign_in_grid_xpath)))
        sign_in_link = self.driver.find_element(By.XPATH, self.link_sing_in_xpath)
        sign_in_link.click()

    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, self.button_signIn_css)
        sign_in_button.click()
        time.sleep(2)

    def click_customer_toggle_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_customer_menu_css).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_signOut_xpath).click()
        time.sleep(10)
