import allure
from pages.password_recovery_page import RecoveryPage
class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_go_to_the_password_recovery_page(self, driver):
        password_recovery = RecoveryPage(driver)
        password_recovery.go_to_personal_acc_botton()
        password_recovery.wait_email_input_field()
        password_recovery.click_restore_tab()
        password_recovery.wait_click_restore_botton()
        actual_url = password_recovery.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title('Проверка восстановления пароля')
    def test_recover_password(self, driver):
        password_recovery = RecoveryPage(driver)
        password_recovery.go_to_personal_acc_botton()
        password_recovery.wait_email_input_field()
        password_recovery.click_restore_tab()
        password_recovery.wait_click_restore_botton()
        password_recovery.fill_out_email()
        password_recovery.click_restore_button()
        password_recovery.wait_save_tub()
        actual_url = password_recovery.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.title('Проверка видимости пароля')
    def test_password_visibility(self, driver):
        password_recovery = RecoveryPage(driver)
        password_recovery.go_to_personal_acc_botton()
        password_recovery.wait_email_input_field()
        password_recovery.click_restore_tab()
        password_recovery.wait_click_restore_botton()
        password_recovery.fill_out_email()
        password_recovery.click_restore_button()
        password_recovery.wait_save_tub()
        password_recovery.fill_out_password()
        password_recovery.click_visibility_password()
        password_recovery.wait_not_visibility_password_tub()
        element = password_recovery.not_visibility_password_tub()
        assert element.get_attribute('class') == 'input__placeholder text noselect text_type_main-default input__placeholder-focused input__placeholder-filled'





