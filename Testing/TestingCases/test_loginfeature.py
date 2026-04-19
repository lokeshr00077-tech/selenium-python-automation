import pytest

from TestingPages.Loginpage import Loginpage
from conftest import *


@pytest.mark.usefixtures("browser_setup")
class Test_login:
    def SetUp_class(self):
        self.driver.get(BaseUrl)
        self.login_page = Loginpage(self.driver)


    def test_valid_login(self):
        self.SetUp_class()
        self.login_page.login(Username,Password)

obj= Test_login()

