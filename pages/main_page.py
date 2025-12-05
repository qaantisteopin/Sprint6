from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Получить длину FAQ")
    def get_accordion_len(self):
        accordion = self.wait_and_find_elements(MainPageLocators.FAQ_QUESTIONS)
        return len(accordion)

    def accept_cookie(self):
        self.wait_and_click(MainPageLocators.COOKIE_BUTTON)

    def get_accordion_answer(self, index):
        elements = self.wait_and_find_elements(MainPageLocators.FAQ_QUESTIONS)
        self.wait_and_click_element(elements[index])
        answer = self.wait_and_find_element(MainPageLocators.FAQ_ANSWERS[index])
        return answer.text
    
    @allure.step("Проверить пункт FAQ")
    def get_answer_for_question(self, question_text: str) -> str:
        questions = self.wait_and_find_elements(MainPageLocators.FAQ_QUESTIONS)
        target_index = None
        for i, el in enumerate(questions):
            if el.text.strip() == question_text.strip():
                target_index = i
                break
        assert target_index is not None, f'Вопрос "{question_text}" не найден в FAQ'
        return self.get_accordion_answer(target_index)
    
    @allure.step("Открыть форму заказа самоката через шапку")
    def open_header_scooter_order_form(self):
        self.wait_and_click(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Открыть форму заказа самоката через кнопку в середине страницы")
    def open_middle_button_scooter_order_form(self):
        self.wait_and_click(MainPageLocators.MIDDLE_ORDER_BUTTON)

    @allure.step("Кликнуть по лого Яндекса")
    def open_yandex_dzen(self):
        self.wait_and_click(MainPageLocators.YANDEX_LOGO)
        self.switch_window()

    def check_order(self):
        self.wait_and_click(MainPageLocators.TRACK_ORDER_BUTTON)