import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import data

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--window-size=1400,1800")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(options=options, service=service)

    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
        browser.maximize_window()

    browser.get(data.Data.url)
    yield browser
    browser.quit()
