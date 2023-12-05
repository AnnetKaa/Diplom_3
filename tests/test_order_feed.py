import allure
from pages.order_feed_page import OrderFeed
class TestOrderFeed:

    @allure.title('Проверка раскрытия окна заказов')
    def test_go_to_the_order_feed_page(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.click_order_feed_tab()
        order_feed.click_last_order()
        element = order_feed.check_element()
        assert element.text == 'Cостав'

    @allure.title('Проверка отображения заказов в разделах «История заказов» и «Лента заказов»')
    def test_add_ingredient(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.click_personal_area_tab()
        order_feed.fill_authorization_fields()
        order_feed.click_login_tab()
        order_feed.choose_ingredient_tab()
        order_feed.click_make_order_tab()
        order_feed.click_close_window()
        order_feed.click_personal_area_tab_when_autorizied()
        order_feed.click_history_tab()
        number_of_order_in_history = order_feed.make_number_of_order()
        order_feed.click_order_feed_tab_upstairs()
        number_of_order_in_feed = order_feed.make_number_of_order_feed()
        assert number_of_order_in_feed == number_of_order_in_history

    @allure.title('Проверка работы счетчика выполнено за все время')
    def test_all_time_counter(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.click_personal_area_tab()
        order_feed.fill_authorization_fields()
        order_feed.click_login_tab()
        order_feed.click_order_feed_tab()
        number_before = order_feed.make_number_order_for_all_time()
        order_feed.click_translator_tab()
        order_feed.choose_ingredient_tab()
        order_feed.click_make_order_tab()
        order_feed.click_close_window()
        order_feed.click_order_feed_tab()
        number_after = order_feed.make_number_order_for_all_time()
        assert number_before < number_after

    @allure.title('Проверка работы счетчика выполнено за все сегодня')
    def test_today_counter(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.click_personal_area_tab()
        order_feed.fill_authorization_fields()
        order_feed.click_login_tab()
        order_feed.click_order_feed_tab()
        number_before = order_feed.make_number_order_for_today()
        order_feed.click_translator_tab()
        order_feed.choose_ingredient_tab()
        order_feed.click_make_order_tab()
        order_feed.click_close_window()
        order_feed.click_order_feed_tab()
        number_after = order_feed.make_number_order_for_today()
        assert number_before < number_after

    @allure.title('Проверка добавления заказа в раздел в работе')
    def test_order_in_work(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.click_personal_area_tab()
        order_feed.fill_authorization_fields()
        order_feed.click_login_tab()
        order_feed.choose_ingredient_tab()
        order_feed.click_make_order_tab()
        number_of_order = order_feed.make_num_order()
        order_feed.click_close_window()
        order_feed.click_order_feed_tab()
        number_of_order_in_work = order_feed.make_num_order_in_work()
        assert number_of_order == number_of_order_in_work


