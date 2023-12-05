import allure
from pages.password_recovery_page import RecoveryPage
class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_go_to_the_password_recovery_page(self, driver):
        password_recovery = RecoveryPage(driver)
        password_recovery.go_to_personal_acc_botton()
        password_recovery.click_restore_tab()
        actual_url = password_recovery.find_actual_url()
        assert actual_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title('Проверка восстановления пароля')
    def test_recover_password(self, driver):
        password_recovery = RecoveryPage(driver)
        password_recovery.go_to_personal_acc_botton()
        password_recovery.click_restore_tab()
        password_recovery.fill_out_email()
        password_recovery.click_restore_button()
        new_password = password_recovery.new_password()
        assert new_password.text == 'Восстановление пароля'

    @allure.title('Проверка видимости пароля')
    def test_password_visibility(self, driver):
        password_recovery = RecoveryPage(driver)
        password_recovery.go_to_personal_acc_botton()
        password_recovery.click_restore_tab()
        password_recovery.fill_out_email()
        password_recovery.click_restore_button()
        password_recovery.fill_out_password()
        password_recovery.click_visibility_password()
        element = password_recovery.not_visibility_password_tub()
        assert 'input__placeholder' in element.get_attribute('class')




