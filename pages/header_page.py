import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по логотипу "Самокат"')
    def click_on_scooter_logo(self):
        self.click_on_element(HeaderPageLocators.SCOOTER_LOGO)
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по логотипу "Яндекс"')
    def click_on_yandex_logo(self):
        self.click_on_element(HeaderPageLocators.YANDEX_LOGO)
