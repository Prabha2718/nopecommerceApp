import pytest
import allure
from selenium import webdriver
from pageobjects.loginPage import LoginPage
from Utilites.readProperites import ReadConfig
from Utilites.customLogger import LogGen
from TestCases.conftest import setUp


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepageTitle(self, setUp):

        self.logger.info("************* Test_001_login ************")
        self.logger.info("************* Verifying Home Page title ************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Verifying Home Page title Passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("************* Verifying Home Page title Failed ************")
            assert False

    @pytest.mark.regression
    def test_login(self, setUp):
        self.logger.info("************* Test_001_login ************")
        self.logger.info("************* login started************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* login Passed************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************* login Failed************")
            assert False
