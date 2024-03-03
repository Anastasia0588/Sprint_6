from selenium.webdriver.common.by import By


class MainPageLocators:

    # локатор вопросов
    QUESTION = By.ID, 'accordion__heading-{}'
    # локатор ответов
    ANSWER = By.ID, 'accordion__panel-{}'
    # кнопка подтверждения куки "Да все привыкли"
    COOKIE_BUTTON = By.ID, 'rcc-confirm-button'
    # кнопка "Заказать" в хедере
    ORDER_BUTTON_HEADER = [By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]']
    # кнопка "Заказать" на странице
    ORDER_BUTTON_IN_PAGE = [By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]']


