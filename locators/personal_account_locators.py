from selenium.webdriver.common.by import By

class PersonalAccLocators:
    PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
    Email = (By.XPATH, ".//input[@name='name']")
    PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    HISTORY_ORDERS = (By.XPATH, ".//a[text() = 'История заказов']")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
    MAKE_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
