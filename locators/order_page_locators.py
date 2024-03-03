from selenium.webdriver.common.by import By


class OrderPageLocators:

    # поле ввода Имени
    NAME_FIELD = By.XPATH, './/input[@placeholder="* Имя"]'
    # поле ввода Фамилии
    LAST_FIELD = By.XPATH, './/input[@placeholder="* Фамилия"]'
    # поле ввода Адреса
    ADDRESS_FIELD = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'
    # поле ввода Станции метро
    METRO_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]'
    # станция метро
    METRO_STATION = By.XPATH, '//div[text()="{}"]'
    # поле ввода номера телефона
    PHONE_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]'
    # кнопка "Далее"
    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'
    # поле выбора даты
    DATE_FIELD = By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]'
    # текущая дата
    CHOOSE_DATE = By.CLASS_NAME, "react-datepicker__day--today"
    # поле ввода срока аренды
    DURATION_FIELD = By.CLASS_NAME, "Dropdown-root"
    # поле выбора срока аренды
    DURATION_RENT = By.XPATH, './/div[@class = "Dropdown-option" and text()="двое суток"]'
    # выбор черного жемчуга
    SCOOTER_COLOR = By.XPATH, './/input[@id="{}"]/parent::label'
    # выбор серой безысходности
    GREY_COLOR = By.ID, "grey"
    # кнопка оформления заказа
    ORDER_BUTTON = By.XPATH, './/*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    # кнопка подтверждения
    CONFIRM_BUTTON = By.XPATH, './/button[text()="Да"]'
    # кнопка просмотра заказа
    ORDER_COMPLETE = By.XPATH, './/*[contains(@class,"Order_ModalHeader")]'
