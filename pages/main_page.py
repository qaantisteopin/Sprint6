from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Получить длину FAQ")
    def get_accordion_len(self):
        accordion = self.wait_and_find_elements(MainPageLocators.FAQ_QUESTIONS)
        return len(accordion)

    @allure.step("Проверить пункт FAQ")
    def get_accordion_answer(self, index):
        elements = self.wait_and_find_elements(MainPageLocators.FAQ_QUESTIONS)
        self.wait_and_click_element(elements[index])
        answer = self.wait_and_find_element(MainPageLocators.FAQ_ANSWERS[index])
        return answer.text