import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def go_to(self, link):
        self.driver.get(link)

    @allure.step('Нажимаем на вопрос')
    def click_to_question(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        self.find_element_with_wait((method, locator))
        self.click_on_element((method, locator))

    @allure.step('Получаем текст ответа')
    def get_answer(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        element = self.find_element_with_wait((method, locator))
        return self.get_text_from_element(element)

    @allure.step('Кликаем по кнопке подтверждения куки "Да все привыкли"')
    def click_cookie_button(self, locator=MainPageLocators.COOKIE_BUTTON):
        self.find_element_with_wait(locator)
        self.click_on_element(locator)

    @allure.step('Кликаем по кнопке "Заказать" в хедере')
    def click_order_button_in_header(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER).click()

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_order_button_in_page(self):
        self.scroll_and_click_with_wait(MainPageLocators.ORDER_BUTTON_IN_PAGE)



