from selenium.webdriver.common.by import By
import time

class iJad_felan_page():
    # its a normal pythonn class so we should define constructor
    #there are few thing i want to provide to this class  to work on the element

    def __init__(self, driver):
          #provide driver instance - chon hame karaye find element click element ke marbod be driver hast ro mikhaym inja ham anjam bedim
        self.driver = driver


    #locator
    _emailText_Field = "//input[@placeholder='Email, e.g. bilbo@example.com']"
    _passwordText_Field = "//div[@class='form-group']//input[@placeholder='Password, e.g. •••••••••••••••••']"
    _login_Button = "//button[contains(text(),'LOGIN')]"
    _badan_button = "//button[contains(text(),'بعدا')]"
    _ijadProje = "//h4[contains(text(),'پروژه‌های شخصی')]//following-sibling::button"
    _onvanProje ="//input[@placeholder='عنوان پروژه']"
    _besazButton = "//button[@class='btn raised primary pull-right']"

    #expose upper locators in to web element by defining function
    #this element then can be utelize in any number of methond
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
