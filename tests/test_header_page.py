import allure

import links

from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage

import pytest


class TestHeaderPage:

    @allure.title('Проверка перехода на главную страницу по нажатию на логотип "Самокат"')
    @allure.description('Выполняется переход со страницы заказа на главную по нажатию на логотип "Самокат"')
    def test_scooter_logo(self, driver):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        header_page = HeaderPage(driver)

        main_page.click_cookie_button()
        main_page.click_order_button_in_header()
        order_page.find_name_field()
        header_page.click_on_scooter_logo()
        result_url = header_page.get_current_url()

        assert result_url == links.main_page


    @allure.title('Проверка открытие через редирект страницы Дзан по нажатию на логотип "Яндекс"')
    @allure.description('По нажатию на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена".')
    def test_yandex_logo(self, driver):

        main_page = MainPage(driver)
        header_page = HeaderPage(driver)

        main_page.click_cookie_button()
        header_page.click_on_yandex_logo()
        header_page.switch_pages()
        result_url = header_page.get_current_url()

        assert result_url == links.dzen_page
