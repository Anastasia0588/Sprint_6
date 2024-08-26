import allure
import pytest

import testdata
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка соответствия вопросов и ответов')
    @allure.description('Позитивный сценарий: по нажатию на стрелочку, открывается соответствующий текст ответа')
    @pytest.mark.parametrize("number, expected_result",
                             [
                                 (0, testdata.answer[0]),
                                 (1, testdata.answer[1]),
                                 (2, testdata.answer[2]),
                                 (3, testdata.answer[3]),
                                 (4, testdata.answer[4]),
                                 (5, testdata.answer[5]),
                                 (6, testdata.answer[6]),
                                 (7, testdata.answer[7])
                             ])
    def test_questions(self, driver, number, expected_result):

        main_page = MainPage(driver)

        main_page.click_cookie_button()
        main_page.scroll_to_bottom_page()
        main_page.click_to_question(MainPageLocators.QUESTION, number)
        result = main_page.get_answer(MainPageLocators.ANSWER, number)

        assert result == expected_result

