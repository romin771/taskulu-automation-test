from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from pages.home.login_page import loginPage
import unittest
import time
import pytest


@pytest.mark.usefixtures("OneTimeSetUp","setUp")
class loginTests(unittest.TestCase):

    #driverlocation = "/Users/romin/Desktop/selenium/chromedriver"
    #os.environ["webdriver.chrome.driver"] = driverlocation
    #driver = webdriver.Chrome(driverlocation)
    baseURL = "https://taskulu.com/account/login?go=login"
    #driver.maximize_window()
    #driver.implicitly_wait(3)
    #driver.get(baseURL)

    # ----------------------------------------
    #for this login page object, we need class level setup
    #i want this only in my login test classes
    #we should make a classLevelSetup using Pytest Fixture

    #lp = loginPage(driver)
    # ----------------------------------------
    #here we have classlevel setup = an object for login page
    @pytest.fixture(autouse=True)
    def classSetup(self, OneTimeSetUp):
        self.lp = loginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(self.baseURL)
        self.lp.Login("romin@taskulu.com", "Romin123456789")
        userIcon = self.lp.verifySuccessfulLogin()
        time.sleep(5)
        assert userIcon == True

        """ 
        userIcon = self.driver.find_element(By.XPATH, "//div[@class='user-avatar has-chat-status default text']")
        if userIcon is not None:
            print("login Successul ")
        else:
            print("login Failed")
             
             
             //i have create a method for this in login_page called verifysuccessfulLogin
        """

        badan = self.driver.find_element(By.XPATH, "//button[contains(text(),'بعدا')]")
        badan.click()


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        #self.driver.get(self.baseURL)
        self.lp.Login("romin@taskulu.com", "Romin123jkjhkjhkj456789")
        error = self.lp.verifyFailLogin()
        time.sleep(5)
        assert error == True


