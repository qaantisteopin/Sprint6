from pages.main_page import MainPage
from data import MainPageData
import allure


@allure.epic('Тесты главной страницы')
class TestMainPage():
    @allure.title('Проверка FAQ на главной странице')
    @allure.description('Кликаем по элементу FAQ, получаем ответ, сверяем ответ с эталоном')
    def test_faq_accordion(self, driver):
        main_page = MainPage(driver)
        template_length = len(MainPageData.EXPECTED_FAQ)
        accordion_length = main_page.get_accordion_len()
        assert accordion_length == template_length, "Количество вопросов не соответствует количеству эталонных ответов"
        for i in range(accordion_length):
            answer = main_page.get_accordion_answer(i)
            assert answer == MainPageData.EXPECTED_FAQ[i], "Ответ на вопрос не сходится с эталоном"
        