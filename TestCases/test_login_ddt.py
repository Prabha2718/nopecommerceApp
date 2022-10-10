import time

import pytest
import allure
from selenium import webdriver
from pageobjects.loginPage import LoginPage
from Utilites.readProperites import ReadConfig
from Utilites.customLogger import LogGen
from TestCases.conftest import setUp
from Utilites import XLUtils


class Test_002_DDT_login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/login.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setUp):
        self.logger.info("************* Test_002_DDT_login ************")
        self.logger.info("************* login started************")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("no of rows:", self.rows)

        lst_status = []

        for r in range(2, self.rows ):
            print(r)
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("****** passed*****")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp == 'fail':
                    self.logger.info("****** Failed*****")
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("****** failed *****")
                    lst_status.append("fail")
                elif self.exp == 'Fail':
                    self.logger.info("****** passed*****")
                    self.lp.clickLogout()
                    lst_status.append("pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test is failed")
            self.driver.close()
            assert False

        self.logger.info("********* End of login DDT test ***********")
        self.logger.info("********* Completed  Test_002_DDT_login ***********")
