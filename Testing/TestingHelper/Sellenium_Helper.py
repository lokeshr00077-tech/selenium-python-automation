from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sellenium_Helper:
    def __init__(self, driver):
        self.driver = driver


    def Webelement_entre(self, locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def Webelement_click(self, locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()