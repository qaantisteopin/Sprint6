from pages.main_page import MainPage
from data import MainPageData, Urls
import allure
import pytest


@allure.epic('Тесты главной страницы')
class TestMainPage:

    @allure.title('Проверка длины FAQ на главной странице')
    @allure.description('Считаем количество элементов FAQ, сравниваем с количеством ключей в эталоне')
    def test_faq_count(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        expected = MainPageData.EXPECTED_FAQ
        accordion_length = main_page.get_accordion_len()
        assert accordion_length == len(expected), "Количество вопросов не соответствует количеству эталонных вопросов"
    
    @pytest.mark.parametrize("question, expected_answer",MainPageData.EXPECTED_FAQ.items())
    @allure.title('Проверка ответа FAQ: {question}')
    @allure.description('Принимаем куки, кликаем по элементу FAQ, получаем ответ, сверяем ответ с эталоном')
    def test_faq_accordion_param(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        actual_answer = main_page.get_answer_for_question(question)
        assert actual_answer == expected_answer, \
            "Ответ на вопрос не сходится с эталоном"
        
    @allure.title('Проверка перехода на страницу Дзена')
    @allure.description('Принимаем куки, кликаем по логотипу Яндекса в шапке, сравниваем URL')
    def test_open_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.open_yandex_dzen()
        current_url = main_page.get_current_url()
        assert current_url == Urls.DZEN_REDIRECT_URL
    
    @allure.title('Проверка открытия страницы заказа через кнопку на странице')
    @allure.description('Принимаем куки, открываем форму заказа через кнопку на странице, сравниваем URL')
    def test_open_scooter_order_page_from_middle_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.open_middle_button_scooter_order_form()
        current_url = main_page.get_current_url()
        assert current_url == Urls.MESTO_ORDER_PAGE_URL
