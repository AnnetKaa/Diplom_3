import allure
from selenium.webdriver.common import action_chains

from pages.base_page import BasePage
from locators import main_functionality_locators
import data

class MainPage(BasePage):
    locators = main_functionality_locators.MainFuncLocators()

    @allure.step('Проверка перехода по кнопке Конструктор')
    def click_translator_tab(self):
        self.find_element(self.locators.TRANSLATOR_TUB).click()

    @allure.step('Проверка перехода по Личный кабинет')
    def click_personal_area_tab(self):
        self.find_element(self.locators.PERSONAL_AREA).click()

    @allure.step('Ожидание кнопки Войти')
    def wait_click_login_botton(self):
        self.wait_element_to_be_clickable(self.locators.LOGIN_BUTTON)

    @allure.step('Переход на вкладку Лента заказов')
    def click_order_feed_tab(self):
        self.find_element(self.locators.ORDER_FEED).click()

    @allure.step('Ожидание заказов')
    def wait_click_order_botton(self):
        self.wait_element_to_be_clickable(self.locators.ORDER)

    @allure.step('Нажать на ингредиент')
    def click_ingredient_tab(self):
        self.find_element(self.locators.INGREDIENT).click()

    @allure.step('Ожидание кнопки выхода')
    def wait_click_exit_botton(self):
        self.wait_element_to_be_clickable(self.locators.EXIT_TAB)

    @allure.step('Определение класса Выход')
    def class_exit_tub(self):
        return self.find_element(self.locators.EXIT_TAB)

    @allure.step('Нажать Выход')
    def click_exit_tub(self):
        return self.find_element(self.locators.EXIT_TAB)

    @allure.step('Ожидание кнопки Соусы')
    def wait_sauses_botton(self):
        self.wait_element_to_be_clickable(self.locators.SAUSES_BUTTON_PARENT)

    @allure.step('Проверка закрытия окна')
    def check_not_window(self):
        return self.find_element(self.locators.CLOSED_WINDOW)

    @allure.step('Проверить количество заказов')
    def order_count(self):
        count = self.find_element(self.locators.ORDER_COUNT)
        return count.text

    @allure.step('Проверка переноса ингредиента')
    def choose_ingredient_tab(self):
        ingredient = self.driver.find_element(*self.locators.INGREDIENT_MOVE)
        add_to_order = self.driver.find_element(*self.locators.ADD_TO_ORDER)
        return self.action.drag_and_drop(ingredient, add_to_order).perform()

    @allure.step('Ожидание, что ингредиент добавился')
    def wait_ingridients(self):
        self.wait_element_to_be_clickable(self.locators.INGREDIENT_MOVE)

    @allure.step('Заполнить данные для авторизации')
    def fill_authorization_fields(self):
        self.find_element(self.locators.Email).send_keys(*data.Data.email)
        self.find_element(self.locators.PASSWORD).send_keys(*data.Data.password)

    @allure.step('Нажать войти')
    def click_login_tab(self):
        self.find_element(self.locators.LOGIN_BUTTON).click()

    @allure.step('Ожидание кнопки сделать заказ')
    def wait_make_order_button(self):
        self.wait_element_to_be_clickable(self.locators.MAKE_ORDER)

    @allure.step('Нажать сделать заказ')
    def click_make_order_tab(self):
        self.find_element(self.locators.MAKE_ORDER).click()

    @allure.step('Ожидание номера заказа')
    def wait_visibility_order_identifier(self):
        self.wait_presence_of_element_located(self.locators.ORDER_IDENTIFIER)

    @allure.step('Проверить наличие элемента')
    def check_order_identifier(self):
        return self.find_element(self.locators.ORDER_IDENTIFIER)










