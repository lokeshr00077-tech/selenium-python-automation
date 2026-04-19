
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class alert():

    def launch(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.facebook.com/")









obj=alert()
obj.launch()
