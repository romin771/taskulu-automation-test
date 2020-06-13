import pytest
from selenium import webdriver
import os
from base.webdriverFactory import WebDriverFactory

@pytest.yield_fixture()  #run before and after
def setUp():
    print("running conftest demo 1 method Setup")
    yield               #anything after this keyword , run after tests
    print("running conftest demo 1 method teardownd")



@pytest.yield_fixture(scope="class")
def OneTimeSetUp(request, browser):
    #here we can make options we want to read from comment line
    print("running one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    """ 
    if browser == "chrome":
        #when we have chrome, we want a variable to provide in test instance class
        #driverlocation = "/Users/romin/Desktop/selenium/chromedriver"
        #os.environ["webdriver.chrome.driver"] = driverlocation
        #driver = webdriver.Chrome(driverlocation)
        #baseURL = "https://taskulu.com/account/login?go=login"
        #driver.maximize_window()
        #driver.implicitly_wait(4)
        #driver.get(baseURL)

        print("running test on ff")
    else:

        driverlocation = "/Users/romin/Desktop/selenium/chromedriver"
        driver = webdriver.Chrome(driverlocation)
        baseURL = "https://taskulu.com/account/login?go=login"
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(baseURL)
        print("running on chrome ") """

    #return driver ----------------------------
    if request.cls is not None:
        request.cls.driver = driver

    # RETURN DRIVER  = i can user same driver instance in my test classes and page classes
    yield driver

    driver.quit()
    print("running conftest demo once after all tests ")
    # return driver ----------------------------


#----------------------------- ye chizi sakhtim az terminal betonim dastor begirim
def pytest_addoption(parser):
    parser.addoption("--browser") #we add option to the parser / what ever option we want the comment line to do
    parser.addoption("--osType", help="type of operating system ")

#ye fixture sakhtim azin
#take options and set fixture
#method : getoption   --> this get the option
@pytest.yield_fixture(scope="session") #sesstion is multiple of module
def browser(request): #request undestant what its gonna take
    return request.config.getoption("--browser")

@pytest.yield_fixture(scope="session")
def browser(request): #request undestant what its gonna take
    return request.config.getoption("--osType")