import string

import pytest
import time
import random

from selenium.webdriver.common.by import By
from TestCases.conftest import random_generator
from pageobjects.loginPage import LoginPage
from pageobjects.AddCustomerPage import AddCustomer
from Utilites.readProperites import ReadConfig
from Utilites.customLogger import LogGen
from TestCases.conftest import setUp


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addcustomer(self, setUp):
        self.logger.info("************* Test_003_AddCustomer ************")
        self.logger.info("************* login started************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* login Passed************")

        self.logger.info("************* Starting Add Customer Test************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        time.sleep(1)
        self.addcust.ClickOnCustomersmenuitem()

        self.addcust.ClickOnAddnew()

        self.logger.info("************* Providing customer info ************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        time.sleep(1)
        self.addcust.setCustomRoles("Guests")
        self.addcust.setManagerOfValues("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Prabhakar")
        self.addcust.setLastName("Pandian")
        self.addcust.setDob("27/03/1994")
        self.addcust.setCompanyName("Selenium test")
        self.addcust.setAdminContent("This is for testing..........")
        self.addcust.ClickOnSave()

        self.logger.info("************* Saving customer info ************")

        self.logger.info("************* Add customer validation info ************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("************* Add customer Test passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_AddCustomer.png")    #screenshot
            self.logger.error("******** Add customer failed *******" )
            assert  True == False

        self.driver.close("************* Ending add customer test passed ************")
        self.logger.info()

    # def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    #     return " ".join(random.choice(chars) for x in range(size))
