import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from data import Data


class TestRegistration:

    def test_registration_with_correct_email_and_pswd_successful(self, driver):
        driver.get(Data.url_registration)

        driver.find_element(*Registration.reg_name).send_keys(Data.reg_name)
        driver.find_element(*Login.login_email).send_keys(Data.reg_email)
        driver.find_element(*Login.login_pass).send_keys(Data.reg_pswd)

        driver.find_element(*Registration.reg_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Login.login_text))

        login_form_text = driver.find_element(*Login.login_text)
        assert login_form_text.text == 'Вход'

    def test_registration_with_incorrect_pswd_show_error(self, driver):
        driver.get(Data.url_registration)

        driver.find_element(*Registration.reg_name).send_keys('Testislav')
        driver.find_element(*Login.login_email).send_keys('test_3009@ya.ru')
        driver.find_element(*Login.login_pass).send_keys('12')

        driver.find_element(*Registration.reg_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Registration.reg_pswd_error))

        error_message = driver.find_element(*Registration.reg_pswd_error)
        assert error_message.text == 'Некорректный пароль'
