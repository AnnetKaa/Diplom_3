import allure
from pages.main_functionality_page import MainPage
class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу Конструктора')
    def test_go_to_the_translator_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_area_tab()
        main_page.click_translator_tab()
        actual_url = main_page.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/'

    @allure.title('Проверка перехода на страницу Ленты Заказов')
    def test_go_to_the_order_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_tab()
        actual_url = main_page.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('Проверка клика ингредиента')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_tab()
        element = main_page.class_exit_tub()
        assert element.get_attribute('class') == 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'

    @allure.title('Проверка закрытия окна ингредиента')
    def test_exit_from_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_tab()
        main_page.click_exit_tub()
        element = main_page.check_not_window()
        assert element.get_attribute('class') == 'Modal_modal__P3_V5'

    @allure.title('Проверка добавления ингредиента в заказ')
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        order_count_before = main_page.order_count()
        main_page.choose_ingredient_tab()
        order_count_after = main_page.order_count()
        assert int(order_count_before) < int(order_count_after)

    @allure.title('Проверка оформления заказа залогиненым пользователем')
    def test_add_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_area_tab()
        main_page.fill_authorization_fields()
        main_page.click_login_tab()
        main_page.choose_ingredient_tab()
        main_page.click_make_order_tab()
        element = main_page.check_order_identifier()
        assert element.text == 'идентификатор заказа'


