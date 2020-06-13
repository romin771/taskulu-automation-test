
from selenium.webdriver.common.by import By
from base.mySeleniumDriver import mySeleniumDriver

    #inherit from mySeleniumDriver class
class loginPage(mySeleniumDriver):

    #define constructor // there is few more things we want to provide to this class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


     #locator
    _email_field = "//input[@placeholder='Email, e.g. bilbo@example.com']"
    _password_field = "//div[@class='form-group']//input[@placeholder='Password, e.g. •••••••••••••••••']"
    _login_button = "//button[contains(text(),'LOGIN')]"
    _user_icon = "//div[@class='user-avatar has-chat-status default text']"

    """ 
    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self._email_field)
    def getPasswordField(self):
        return self.driver.find_element(By.XPATH, self._password_field)
    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button) """


    #actions
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")


    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")
        #self.getPasswordField().send_keys(password)
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")




    #login method
    def Login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()


    def verifySuccessfulLogin(self): #mige iteme avatar to safhe bade login didam. pas login movafagh bode
        userIcon = self.isElementPresent("//div[@class='user-avatar has-chat-status default text']", locatorType="xpath")
        return userIcon  #javabe True ya False barmigardone

    def verifyFailLogin(self):
        errorLogin = self.isElementPresent("//p[contains(text(),'Invalid username or password')]", "xpath")
        return errorLogin

    """
    def ClearField(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear() """




