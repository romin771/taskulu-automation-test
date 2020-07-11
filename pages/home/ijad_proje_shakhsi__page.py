from selenium.webdriver.common.by import By
import time
from base.mySeleniumDriver import mySeleniumDriver


                    #inherit from this class which our custom class
class iJad_felan_page(mySeleniumDriver):
    # its a normal pythonn class so we should define constructor
    #there are few thing i want to provide to this class  to work on the element

    def __init__(self, driver):
        super().__init__(driver)
          #provide driver instance - chon hame karaye find element click element ke marbod be driver hast ro mikhaym inja ham anjam bedim
        self.driver = driver


    #1)locator
    # here it does not matter if its xpath, name , id ... its just locator
    #when ever any locator changes on website, next release or any time, we should just change here. thats it ;)
    _emailText_Field = "//input[@placeholder='Email, e.g. bilbo@example.com']"
    _passwordText_Field = "//div[@class='form-group']//input[@placeholder='Password, e.g. •••••••••••••••••']"
    _login_Button = "//button[contains(text(),'LOGIN')]"
    _badan_button = "//button[contains(text(),'بعدا')]"
    _ijadProje = "//h4[contains(text(),'پروژه‌های شخصی')]//following-sibling::button"
    _onvanProje ="//input[@placeholder='عنوان پروژه']"
    _besazButton = "//button[@class='btn raised primary pull-right']"
    _ijadTodo = "//div[@class='list-tasks-wrapper _view_element']//div[1]//div[1]//i[1]"

    #2)define method to expose locators into element ( find element ...  )
    #expose upper locators in to web element by defining function
    #this element then can be utelize in any number of methond
    """
    Note 1 ) since we creat a function clicking on element and sending data to it in our 
    custom selenium class ( mySeleniumDriver.py) + also we are finding those element 
    inside our framework classes , we can get rid of this lines :
    
    def getEmailTextField(self):
        return self.driver.find_element(By.XPATH, self._emailText_Field)
    def getPasswordTextField(self):
        return self.driver.find_element(By.XPATH, self._passwordText_Field)
    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_Button)
    def getBadanButton(self):
        return self.driver.find_element(By.XPATH, self._badan_button)
    def getIjadProjeButton(self):
        return self.driver.find_element(By.XPATH, self._ijadProje)
    def detOnvanProje(self):
        return self.driver.find_element(By.XPATH, self._onvanProje)
    def getbesazButton(self):
        return self.driver.find_element(By.XPATH, self._besazButton)
    def getijadTODO(self):
        return self.driver.find_element(By.XPATH, self._ijadTodo)"""




    """ based on Note1 which explained above, we can get rid of commented lines 
    
      def enterEmail(self, email):
        #self.getEmailTextField().send_keys(email)
        
        #self.getPasswordTextField().send_keys(passw)
        #self.getLoginButton().click()
        #self.getBadanButton().click()
    """

    #3)actions on elements // CALL THESE FROM OUR CUSTOM SELENIUM WEBDRIVER
    def enterEmail(self, email):
        self.sendKeys(email, self._emailText_Field, locatorType="xpath")
    def enterPassword(self, passw):
        self.sendKeys(passw,self._passwordText_Field, locatorType="xpath")
    def clickLoginButton(self):
        self.elementClick(self._login_Button, locatorType="xpath")
    def clickBadanButton(self):
        self.elementClick(self._badan_button, locatorType="xpath")

    #main functionality // it wrapp the actions together for doing A function
    def login2(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.clickBadanButton()



    #instead of these codes we can come up with uppers  : after creating :
    #1)locators - 2)method to expose - 3)action on methods

    def login(self, username, password):
        emailTextField = self.driver.find_element(By.XPATH, "//input[@placeholder='Email, e.g. bilbo@example.com']")
        emailTextField.send_keys(username)


        passwordTextField = self.driver.find_element(By.XPATH,
                                                     "//div[@class='form-group']//input[@placeholder='Password, e.g. •••••••••••••••••']")
        passwordTextField.send_keys(password)

        loginButton = self.driver.find_element(By.XPATH, "//button[contains(text(),'LOGIN')]").click()

        badan = self.driver.find_element(By.XPATH, "//button[contains(text(),'بعدا')]")
        badan.click()
        ijadProje = self.driver.find_element(By.XPATH,
                                             "//h4[contains(text(),'پروژه‌های شخصی')]//following-sibling::button")
        ijadProje.click()
        time.sleep(2)
        onvanProje = self.driver.find_element(By.XPATH, "//input[@placeholder='عنوان پروژه']")

        onvanProje.send_keys("TestForRomin")

        besazButton = self.driver.find_element(By.XPATH, "//button[@class='btn raised primary pull-right']")
        besazButton.click()

        ijadTodo = self.driver.find_element(By.XPATH, "//div[@class='list-tasks-wrapper _view_element']//div[1]//div[1]//i[1]")
        ijadTodo.click()



