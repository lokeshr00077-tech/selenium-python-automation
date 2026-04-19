import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl= "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username= "Admin"
Password= "admin123"



@pytest.fixture(scope='Class', autouse= True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_argument("detach",True)
    request.cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
