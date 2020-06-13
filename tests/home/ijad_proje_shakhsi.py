from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from pages.home.ijad_proje_shakhsi__page import iJad_felan_page
import unittest


class createNewPersonalProject(unittest.TestCase):

    def test_successfulCreation(self):

        self.driverlocation = "/Users/romin/Desktop/selenium/chromedriver"
        os.environ["webdriver.chrome.driver"] = self.driverlocation
        self.driver = webdriver.Chrome(self.driverlocation)
        baseURL = "https://taskulu.com/account/login?go=login"
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.get(baseURL)

        lp = iJad_felan_page(self.driver)
        lp.login("Romin@taskulu.com", "Romin123456789")



        searchTextField = self.driver.find_element(By.XPATH, "//input[@placeholder='جستجو پروژه‌ها']")
        if searchTextField is not None:
            print("login successful ")
        else:
            print('login failed ')










