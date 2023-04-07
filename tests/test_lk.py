from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def email_password(driver, email, password):
    driver.find_element(By.XPATH, "//label[contains(.,'Email')]/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[contains(.,'Пароль')]/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()


def test_enter_lk(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    personal_message = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[contains(.,'В этом разделе вы можете изменить свои персональные данные')]")))
    assert personal_message.text == 'В этом разделе вы можете изменить свои персональные данные'
    driver.quit()


def test_lk_go_page_constructor(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[contains(.,'В этом разделе вы можете изменить свои персональные данные')]")))
    driver.find_element(By.XPATH, "//p[contains(.,'Конструктор')]").click()
    make_burger = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Соберите бургер')]")))
    assert make_burger.text == "Соберите бургер"
    driver.quit()


def test_lk_go_page_stellar_burgers(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[contains(.,'В этом разделе вы можете изменить свои персональные данные')]")))
    driver.find_element(By.CSS_SELECTOR, "[class*='logo']>a").click()
    make_burger = WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Соберите бургер')]")))
    assert make_burger.text == "Соберите бургер"
    driver.quit()


def test_exit_account(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(.,'Войти в аккаунт')]").click()
    email_password(driver, email, password)
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(.,'Оформить заказ')]")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    WebDriverWait(driver, 4).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[contains(.,'В этом разделе вы можете изменить свои персональные данные')]")))
    driver.find_element(By.XPATH, "//button[contains(.,'Выход')]").click()

    driver.quit()
