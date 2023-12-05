from selenium.webdriver.common.by import By
class LocatorsforPasswordRecovery:
    RESTORE_TAB = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    RESTORE_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    Email = (By.XPATH, ".//input[@name='name']")
    Email_REQUEST_RESTORATION = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    SAVE = (By.XPATH, ".//button[text() = 'Сохранить']")
    PASSWORD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    VISIBILITY_TAB = (By.XPATH, ".//div[@class ='input__icon input__icon-action']")
    NOT_VISIBILITY_TAB = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    CLASS_CHECK = (By.XPATH, ".//label[text() = 'Пароль']")
    NEW_PASSWORD = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
