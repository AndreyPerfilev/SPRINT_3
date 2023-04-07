import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_new_user_positive(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    driver.find_element(By.XPATH, "//label[contains(.,'Имя')]/following-sibling::input").send_keys("Andrey")
    email_value = str(random.randint(0, 99999)) + "@ya.ru"
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys(email_value)
    password_value = "123456789"
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys(password_value)
    driver.find_element(By.XPATH, "//button[contains(.,'Зарегистрироваться')]").click()
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Войти')]")))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys(email_value)
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys(password_value)
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()
    button_order = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    assert button_order.text == "Оформить заказ"
    driver.quit()


def test_registration_password_lower_six(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    driver.find_element(By.XPATH, "//label[contains(.,'Имя')]/following-sibling::input").send_keys("Andrey")
    email_value = str(random.randint(0, 99999)) + "@ya.ru"
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys(email_value)
    password_value = "12345"
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys(password_value)
    driver.find_element(By.XPATH, "//button[contains(.,'Зарегистрироваться')]").click()
    error_element = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p.input__error")))
    assert error_element.text == 'Некорректный пароль'
    driver.quit()
