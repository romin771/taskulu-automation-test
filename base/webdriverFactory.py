
import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser


    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://taskulu.com/account/login?go=login"

        if self.browser == "chrome":
            driver = webdriver.chrome()
        elif self.browser == "chrome":
            # Set chrome driver
            #driver = webdriver.Chrome()
            driverlocation = "/Users/romin/Desktop/selenium/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverlocation
            driver = webdriver.Chrome(driverlocation)
        else:
            driverlocation = "/Users/romin/Desktop/selenium/chromedriver"
            driver = webdriver.Chrome(driverlocation)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver


