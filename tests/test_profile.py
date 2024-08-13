import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


class TestProfileNavigation:

    # Переход по клику на «Личный кабинет».
    def test_click_on_profile_open_personal_account_page(self, login):
        driver = login

        driver.find_element(*Main.main_personal_account).click()
        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(Main.main_profile))

        profile = driver.find_element(*Main.main_profile)
        assert profile.text == 'Профиль'

    # Переход из личного кабинета по клику на «Конструктор»

    def test_click_on_constructor_open_constructor_form(self, login):
        driver = login

        driver.find_element(*Main.main_personal_account).click()
        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(Main.main_profile))
        driver.find_element(*Main.main_constructor).click()
        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(Main.main_burger_text))

        burger_text = driver.find_element(*Main.main_burger_text)
        assert burger_text.text == 'Соберите бургер'

    # Переход из личного кабинета по клику на логотип Stellar Burgers.

    def test_click_on_logo_open_constructor_form(self, login):
        driver = login

        driver.find_element(*Main.main_personal_account).click()
        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(Main.main_profile))
        driver.find_element(*Main.main_logo_button).click()
        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(Main.main_burger_text))

        burger_text = driver.find_element(*Main.main_burger_text)
        assert burger_text.text == 'Соберите бургер'

        # Выход по кнопке «Выйти» в личном кабинете
    def test_logout_profile_logout_successful(self, login):
        driver = login

        driver.find_element(*Main.main_personal_account).click()
        WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located(Main.main_profile))
        driver.find_element(*Main.main_logout_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Login.login_text))

        login_form_text = driver.find_element(*Login.login_text)
        assert login_form_text.text == 'Вход'
