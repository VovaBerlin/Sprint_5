import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from data import Data


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_sign_button_on_main_page_successful_logged(self, driver):
        driver.find_element(*Login.login_button_main_page).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Login.login_text))

        driver.find_element(*Login.login_email).send_keys(Data.person_email)
        driver.find_element(*Login.login_pass).send_keys(Data.person_pass)
        driver.find_element(*Login.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.main_order_button))

        order_button = driver.find_element(*Main.main_order_button)
        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку «Личный кабинет»
    def test_login_personal_account_button_successful_logged(self, driver):
        driver.find_element(*Main.main_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Login.login_text))

        driver.find_element(*Login.login_email).send_keys(Data.person_email)
        driver.find_element(*Login.login_pass).send_keys(Data.person_pass)
        driver.find_element(*Login.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.main_order_button))

        order_button = driver.find_element(*Main.main_order_button)
        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку в форме регистрации
    def test_login_button_in_registration_form_successful_logged(self, driver):
        driver.get(Data.url_registration)

        driver.find_element(*Registration.reg_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Login.login_text))

        driver.find_element(*Login.login_email).send_keys(Data.person_email)
        driver.find_element(*Login.login_pass).send_keys(Data.person_pass)
        driver.find_element(*Login.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.main_order_button))

        order_button = driver.find_element(*Main.main_order_button)
        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку в форме восстановления пароля
    def test_login_button_on_recover_password_form_successful_logged(self, driver):
        driver.get(Data.url_forgot_password)

        driver.find_element(*Registration.reg_login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Login.login_text))

        driver.find_element(*Login.login_email).send_keys(Data.person_email)
        driver.find_element(*Login.login_pass).send_keys(Data.person_pass)
        driver.find_element(*Login.login_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Main.main_order_button))

        order_button = driver.find_element(*Main.main_order_button)
        assert order_button.text == 'Оформить заказ'