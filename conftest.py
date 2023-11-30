import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--window-size=1400,1800")
#     service = Service(ChromeDriverManager().install())
#     browser = webdriver.Chrome(options=options, service=service)
#     browser.get("https://stellarburgers.nomoreparties.site/")
#
#     yield browser
#     browser.quit()

# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     if request.param == "chrome":
#         service = Service(ChromeDriverManager().install())
#         options = Options()
#         options.add_argument("--window-size=1400,1800")
#         browser = webdriver.Chrome(options=options, service=service)
#         browser.get("https://stellarburgers.nomoreparties.site/")
#     if request.param == "firefox":
#         service = GeckoDriverManager().install()
#         browser = webdriver.Firefox(service=Service(service))
#         browser.get("https://stellarburgers.nomoreparties.site/")
#         browser.maximize_window()
#
#     yield browser
#     browser.quit()

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--window-size=1400,1800")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(options=options, service=service)
        browser.get("https://stellarburgers.nomoreparties.site/")
    elif request.param == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.maximize_window()

    yield browser
    browser.quit()
