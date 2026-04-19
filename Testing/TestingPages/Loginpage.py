from selenium.webdriver.common.by import By

from TestingHelper.Sellenium_Helper import Sellenium_Helper


class Loginpage(Sellenium_Helper):

    email_webElement= (By.XPATH, "//input[@placeholder='Username']")
    password_webElement= (By.XPATH, "//input[@name='password']")
    login_webElement= (By.XPATH, "//button")

    def __init__(self, driver):
        super().__init__(driver)


    def login(self, Username, Password):
        self.Webelement_entre(self.email_webElement, Username)
        self.Webelement_entre(self.password_webElement, Password)
        self.Webelement_click(self.login_webElement)
