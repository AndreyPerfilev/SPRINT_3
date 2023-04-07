from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def email_password(driver, email, password):
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()

def test_auth_main_page_positive(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    email_password(driver, email, password)
    button_order = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    assert button_order.text == "Оформить заказ"
    driver.quit()


def test_auth_lk(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    email_password(driver, email, password)
    button_order = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    assert button_order.text == "Оформить заказ"
    driver.quit()


def test_auth_registration(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.LINK_TEXT, "Войти").click()
    email_password(driver, email, password)
    button_order = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    assert button_order.text == "Оформить заказ"
    driver.quit()


def test_auth_restore_pass(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.LINK_TEXT, "Войти").click()
    email_password(driver, email, password)
    button_order = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    assert button_order.text == "Оформить заказ"
    driver.quit()
