from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def email_password(driver, email, password):
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()


def test_constructor_buns(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    current_element = driver.find_element(By.CSS_SELECTOR, "[class*='current']>span")
    assert current_element.text == "Булки"
    driver.quit()


def test_constructor_sauces(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Соусы')]").click()
    current_element = driver.find_element(By.CSS_SELECTOR, "[class*='current']>span")
    assert current_element.text == "Соусы"
    driver.quit()


def test_constructor_fillings(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Начинки')]").click()
    current_element = driver.find_element(By.CSS_SELECTOR, "[class*='current']>span")
    assert current_element.text == "Начинки"
    driver.quit()
