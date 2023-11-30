import allure
from pages.base_page import BasePage
from locators import personal_account_locators
import data

class PersonalAcc(BasePage):
    locators = personal_account_locators.PersonalAccLocators()

    @allure.step('Нажать личный кабинет')
    def click_personal_area_tab(self):
        self.find_element(self.locators.PERSONAL_AREA).click()

    @allure.step('Ожидание кнопки войти')
    def wait_click_login_botton(self):
        self.wait_element_to_be_clickable(self.locators.LOGIN_BUTTON)

    @allure.step('Заполнить поля авторизации')
    def fill_authorization_fields(self):
        self.find_element(self.locators.Email).send_keys(*data.Data.email)
        self.find_element(self.locators.PASSWORD).send_keys(*data.Data.password)

    @allure.step('Нажать войти')
    def click_login_tab(self):
        self.find_element(self.locators.LOGIN_BUTTON).click()

    @allure.step('Нажать История заказов')
    def click_history_tab(self):
        self.find_element(self.locators.HISTORY_ORDERS).click()

    @allure.step('Ожидание кнопки сохранить')
    def wait_click_save_botton(self):
        self.wait_element_to_be_clickable(self.locators.SAVE_BUTTON)

    @allure.step('Нажать выйти')
    def click_exit_tab(self):
        self.find_element(self.locators.EXIT_BUTTON).click()

    @allure.step('Ожидание элемента Сделать заказ')
    def wait_make_order_button(self):
        self.wait_element_to_be_clickable(self.locators.MAKE_ORDER)