import pytest
from locators import *


class TestConstructor:

    # Проверка перехода к разделу "Начинки"
    def test_constructor_click_on_button_filling_scroll_to_filling(self, driver):
        driver.find_element(*Main.main_filling_button).click()
        filling = driver.find_element(*Main.main_filling_text)
        assert filling.text == 'Начинки'

    # Проверка перехода к разделу "Соусы"
    def test_constructor_click_on_button_sauce_scroll_to_filling(self, driver):
        driver.find_element(*Main.main_sauce_button).click()
        sauce = driver.find_element(*Main.main_sauce_text)
        assert sauce.text == 'Соусы'

    # Проверка перехода к разделу "Булки"

    def test_constructor_click_on_button_bun_scroll_to_filling(self, driver):
        driver.find_element(*Main.main_filling_button).click()
        driver.find_element(*Main.main_bun_button).click()
        bun = driver.find_element(*Main.main_bun_text)
        assert bun.text == 'Булки'
