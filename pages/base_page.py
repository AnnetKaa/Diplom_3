from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_element_to_be_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_presence_of_element_located(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_actual_url(self):
        return self.driver.current_url

    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)






