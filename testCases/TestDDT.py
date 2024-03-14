from pageObjects.LoginPage import LoginPage
from utilities.customeLogger import LogGen
from utilities import XLUtils
import pytest


class TestDDT:
    baseURL = "https://magento.softwaretestingboard.com"
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    def test_user_login(self, setup):
        self.logger.info("******* Starting Login DDT Test **********")
        list_status = []
        # Initialize the driver outside the loop
        driver = setup
        # Read data from Excel sheet
        rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info(f"Number of Rows... {rows}")

        for row in range(2, rows + 1):
            driver.get(self.baseURL)  # Move this outside the loop
            driver.maximize_window()  # Move this outside the loop
            lp = LoginPage(driver)
            email = XLUtils.readData(self.path, 'Sheet1', row, 1)
            password = XLUtils.readData(self.path, 'Sheet1', row, 2)
            expected = XLUtils.readData(self.path, 'Sheet1', row, 3)
            # Perform login
            lp.click_sign_in_link()
            lp.set_email(email)
            lp.set_password(password)
            lp.click_sign_in_button()
            if expected == "Fail":
                self.logger.info("***Passed***")
                list_status.append("Pass")
                # Check if there are more iterations
                if row == rows:
                    self.logger.info("No more iterations. Ending the test.")
                    driver.quit()  # Close the browser
                    break  # Exit the loop
                continue  # Continue to the next iteration
            # Login was expected to pass
            lp.click_customer_toggle_menu()
            lp.click_logout()
            self.logger.info("***Passed***")
            list_status.append("Pass")
            # Check if there are more iterations
            if row == rows:
                self.logger.info("No more iterations. Ending the test.")
                driver.quit()  # Close the browser
                break  # Exit the loop
        # Check the overall status after all iterations are completed
        if "Fail" not in list_status:
            self.logger.info("Login DDT test passed....")
        else:
            self.logger.info("*****Login DDT test failed....*****")
            pytest.fail("Login DDT test failed.")
