import allure

from pages.base_page import BasePage
from locators import order_feed_locators
import data
class OrderFeed(BasePage):
    locators = order_feed_locators.OrderFeedLocators()

    @allure.step('Нажать Лента заказов')
    def click_order_feed_tab(self):
        self.find_element(self.locators.ORDER_FEED).click()

    @allure.step('Ожидание кнопки заказов')
    def wait_click_order_botton(self):
        self.wait_element_to_be_clickable(self.locators.ORDER)

    @allure.step('Нажать заказ')
    def click_last_order(self):
        self.find_element(self.locators.ORDER).click()

    @allure.step('Ожидание всплывающего окна')
    def wait_visibility_modal_window(self):
        self.wait_presence_of_element_located(self.locators.MODAL_WINDOW)

    @allure.step('Проверить элемент')
    def check_element(self):
        return self.find_element(self.locators.COMPOUND)

    @allure.step('Нажать Личный кабинет')
    def click_personal_area_tab(self):
        self.find_element(self.locators.PERSONAL_AREA).click()

    @allure.step('Ожидание кнопки Войти')
    def wait_click_login_botton(self):
        self.wait_element_to_be_clickable(self.locators.LOGIN_BUTTON)

    @allure.step('Заполнить поля авторизации')
    def fill_authorization_fields(self):
        self.find_element(self.locators.Email).send_keys(*data.Data.email)
        self.find_element(self.locators.PASSWORD).send_keys(*data.Data.password)

    @allure.step('Нажать Войти')
    def click_login_tab(self):
        self.find_element(self.locators.LOGIN_BUTTON).click()

    @allure.step('Ожидание кнопки Оформить заказ')
    def wait_make_order_button(self):
        self.wait_element_to_be_clickable(self.locators.MAKE_ORDER)

    @allure.step('Проверка добавления ингредиента в корзину')
    def choose_ingredient_tab(self):
        ingredient = self.driver.find_element(*self.locators.INGREDIENT_MOVE)
        add_to_order = self.driver.find_element(*self.locators.ADD_TO_ORDER)
        return self.action.drag_and_drop(ingredient, add_to_order).perform()

    @allure.step('Нажать оформить заказ')
    def click_make_order_tab(self):
        self.find_element(self.locators.MAKE_ORDER).click()

    @allure.step('Ожидание элемента на окне заказа')
    def wait_visibility_order_identifier(self):
        self.wait_presence_of_element_located(self.locators.ORDER_IDENTIFIER)

    @allure.step('Нажать закрыть окно')
    def click_close_window(self):
        self.find_element(self.locators.CLOSE_WINDOW).click()

    @allure.step('Нажать История заказов')
    def click_history_tab(self):
        self.find_element(self.locators.HISTORY_ORDERS).click()

    @allure.step('Ожидание кнопки Сохранить')
    def wait_click_save_botton(self):
        self.wait_element_to_be_clickable(self.locators.SAVE_BUTTON)

    @allure.step('Ожидание заказа в списке')
    def wait_click_order_in_list(self):
        self.wait_element_to_be_clickable(self.locators.ORDER_IN_LIST)

    @allure.step('Скролл страницы вниз')
    def scroll_to_last_order(self):
        element = self.find_elements(self.locators.FIND_ORDER)
        self.scroll(element[-1])

    @allure.step('Получить номер заказа')
    def make_number_of_order(self):
        element = self.find_elements(self.locators.NUMBER_ORDER)
        last_element_text = element[-1].text
        return last_element_text

    @allure.step('Скролл страницы наверх')
    def scroll_to_order_feed(self):
        element = self.find_element(self.locators.ORDER_FEED)
        self.scroll(element)

    @allure.step('Получить номер заказа в Ленте')
    def make_number_of_order_feed(self):
        element = self.find_elements(self.locators.NUMBER_ORDER_IN_FEED)
        return element[0].text

    @allure.step('Получить номер заказа за все время')
    def make_number_order_for_all_time(self):
        element = self.find_element(self.locators.COMPLETED_FOR_ALL_TIME)
        return element.text

    @allure.step('Нажать конструктор')
    def click_translator_tab(self):
        self.find_element(self.locators.TRANSLATOR_TUB).click()

    @allure.step('Получить номер заказа за сегодня')
    def make_number_order_for_today(self):
        element = self.find_elements(self.locators.COMPLETED_FOR_ALL_TIME)
        return element[-1].text

    @allure.step('Получить номер заказа при оформлении')
    def make_num_order(self):
        element = self.find_element(self.locators.NUM_ORDER)
        return element.text

    @allure.step('Получить номер заказа в работе')
    def make_num_order_in_work(self):
        element = self.find_element(self.locators.NUM_ORDER_IN_WORK)
        return element.text

    @allure.step('Ожидание заказа в работе')
    def wait_visibility_list_orders_in_work(self):
        self.wait_presence_of_element_located(self.locators.LIST_ORDERS_IN_WORK)






