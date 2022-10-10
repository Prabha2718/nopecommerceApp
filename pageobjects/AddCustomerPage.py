import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "(//a[@href='/Admin/Customer/List'])[1]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = " //input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompany_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    drpManagerOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    lstitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(), 'Registered')]"
    lstitemForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lstitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors')]"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def ClickOnCustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def ClickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.lstitemGuests_xpath,
                                     "(//span[@title='delete'])[1]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfValues(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(lname)

    def setDob(self, Dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(Dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompany_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
