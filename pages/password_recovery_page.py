import allure
from pages.base_page import BasePage
from locators import password_recovery_locators
import data

class RecoveryPage(BasePage):
    locators = password_recovery_locators.LocatorsforPasswordRecovery()

    @allure.step('Нажать восстановить пароль')
    def click_restore_tab(self):
        self.find_element(self.locators.RESTORE_TAB).click()
        self.find_element(self.locators.RESTORE_BUTTON)
        self.wait_element_to_be_clickable(self.locators.RESTORE_BUTTON)

    @allure.step('Нажать личный кабинет')
    def go_to_personal_acc_botton(self):
        self.find_element(self.locators.PERSONAL_AREA).click()
        self.wait_element_to_be_clickable(self.locators.Email)


    @allure.step('Заполнить поле')
    def fill_out_email(self):
        self.find_element(self.locators.Email_REQUEST_RESTORATION).send_keys(*data.Data.email_if_foget)

    @allure.step('Нажать восстановить')
    def click_restore_button(self):
        self.find_element(self.locators.RESTORE_BUTTON).click()
        self.wait_element_to_be_clickable(self.locators.SAVE)

    @allure.step('Ввести пароль')
    def fill_out_password(self):
        self.find_element(self.locators.PASSWORD).send_keys(*data.Data.password)

    @allure.step('Проверить видимость пароля')
    def click_visibility_password(self):
        self.find_element(self.locators.VISIBILITY_TAB).click()
        self.wait_presence_of_element_located(self.locators.NOT_VISIBILITY_TAB)

    @allure.step('Проверить класс')
    def not_visibility_password_tub(self):
        return self.find_element(self.locators.CLASS_CHECK)

    @allure.step('Переход на восстановление пароля')
    def new_password(self):
        return self.find_element(self.locators.NEW_PASSWORD)

