import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def fill_name_filed(self, name):
        self.set_text_to_form(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Находим поле "Имя')
    def find_name_field(self):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD)

    def fill_last_name_field(self, last_name):
        self.set_text_to_form(OrderPageLocators.LAST_FIELD, last_name)

    def fill_address_field(self, address):
        self.set_text_to_form(OrderPageLocators.ADDRESS_FIELD, address)

    def set_metro_field(self, metro):
        self.click_on_element(OrderPageLocators.METRO_FIELD)
        method, locator = OrderPageLocators.METRO_STATION
        locator = locator.format(metro)
        self.scroll_and_click_with_wait((method, locator))

    def fill_phone_field(self, phone_number):
        self.set_text_to_form(OrderPageLocators.PHONE_FIELD, phone_number)

    def set_date_or_duration(self, field_locator, value_locator):
        self.click_on_element(field_locator)
        self.click_on_element(value_locator)

    def choose_scooter_color(self, locator, color):
        method, locator = locator
        locator = locator.format(color)
        self.click_on_element((method, locator))

    @allure.step('Заполняем форму данными пользователя')
    def fill_user_data_form(self, name, last_name, address, metro, phone_number):
        self.fill_name_filed(name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.set_metro_field(metro)
        self.fill_phone_field(phone_number)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем форму деталей заказа данными')
    def set_order_details_and_confirm(self, scooter_color):
        self.set_date_or_duration(OrderPageLocators.DATE_FIELD, OrderPageLocators.CHOOSE_DATE)
        self.set_date_or_duration(OrderPageLocators.DURATION_FIELD, OrderPageLocators.DURATION_RENT)
        self.choose_scooter_color(OrderPageLocators.SCOOTER_COLOR, scooter_color)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Проверяем, что появилось сообщение об успешном заказе')
    def get_text_from_popup(self):
        element = self.find_element_with_wait(OrderPageLocators.ORDER_COMPLETE)
        return self.get_text_from_element(element)




