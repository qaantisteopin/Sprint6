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

    @allure.step("Заполнить форму заказа")
    def fill_order_from(self):
        self.send_keys(MainPageLocators.NAME_ORDER_INPUT, 'Дмитрий')
        self.send_keys(MainPageLocators.SURNAME_ORDER_INPUT, 'Договорнячков')
        self.send_keys(MainPageLocators.ADRESS_ORDER_INPUT, 'ул.Пушкина, д.Колотушкина')
        self.send_keys(MainPageLocators.METRO_ORDER_INPUT, 'Бульвар Рокоссовского')
        self.wait_and_click(MainPageLocators.METRO_OPTION)
        self.send_keys(MainPageLocators.NUMBER_ORDER_INPUT, "+79377781488")
        self.wait_and_click(MainPageLocators.NEXT_ORDER_BUTTON)
        self.send_keys(MainPageLocators.DATE_ORDER_INPUT, '05.12.2025')
        self.wait_and_click(MainPageLocators.CALENDAR_DATE_BUTTON)
        self.wait_and_click(MainPageLocators.RENT_TIME_DROPDOWN)
        self.wait_and_click(MainPageLocators.DROPDOWN_ELEMENT)
        self.wait_and_click(MainPageLocators.ORDER_BUTTON)
        self.wait_and_click(MainPageLocators.CONFIRM_BUTTON_IN_MODAL_WINDOW)
        return self.wait_and_find_element(MainPageLocators.ORDER_BLOCK).text
        
    
    @allure.step("Открыть форму заказа самоката через кнопку в середине страницы")
    def open_middle_button_scooter_order_form(self):
        self.wait_and_click(MainPageLocators.MIDDLE_ORDER_BUTTON)

    @allure.step("Кликнуть по лого Яндекса")
    def open_yandex_dzen(self):
        self.wait_and_click(MainPageLocators.YANDEX_LOGO)
        self.switch_window()

    @allure.step("Кликнуть по лого Самоката")
    def open_scooter_main_page(self):
        self.wait_and_click(MainPageLocators.SCOOTER_LOGO)

    def check_order(self):
        self.wait_and_click(MainPageLocators.TRACK_ORDER_BUTTON)