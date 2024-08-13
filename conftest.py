import pytest
from selenium import webdriver

from data import Data
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.url)
    yield driver
    driver.quit()


@pytest.fixture  # Вход в аккаунт
def login(driver):
    driver.get(Data.url_login)
    driver.find_element(*Login.login_email).send_keys(Data.person_email)
    driver.find_element(*Login.login_pass).send_keys(Data.person_pass)
    driver.find_element(*Login.login_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.main_order_button))
    return driver
