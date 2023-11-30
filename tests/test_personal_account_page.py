import allure
from pages.personal_account_page import PersonalAcc
class TestPasswordRecovery:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_the_personal_area_page(self, driver):
        pers_acc = PersonalAcc(driver)
        pers_acc.click_personal_area_tab()
        pers_acc.wait_click_login_botton()
        actual_url = pers_acc.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/login'

    @allure.title('Проверка перехода на страницу Истории Заказов')
    def test_go_to_the_history_page(self, driver):
        pers_acc = PersonalAcc(driver)
        pers_acc.click_personal_area_tab()
        pers_acc.wait_click_login_botton()
        pers_acc.fill_authorization_fields()
        pers_acc.click_login_tab()
        pers_acc.wait_make_order_button()
        pers_acc.click_personal_area_tab()
        pers_acc.wait_click_save_botton()
        pers_acc.click_history_tab()
        actual_url = pers_acc.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Проверка выхода из аккаунта')
    def test_go_to_the_exit_page(self, driver):
        pers_acc = PersonalAcc(driver)
        pers_acc.click_personal_area_tab()
        pers_acc.wait_click_login_botton()
        pers_acc.fill_authorization_fields()
        pers_acc.click_login_tab()
        pers_acc.wait_make_order_button()
        pers_acc.click_personal_area_tab()
        pers_acc.wait_click_save_botton()
        pers_acc.click_exit_tab()
        pers_acc.wait_click_login_botton()
        actual_url = pers_acc.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/login'