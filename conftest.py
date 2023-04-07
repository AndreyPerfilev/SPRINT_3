import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    return webdriver.Chrome()


@pytest.fixture
def email():
    return "andreyperfilev08@ya.ru"


@pytest.fixture
def password():
    return "123456789"

