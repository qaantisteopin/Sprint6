from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, data: dict):
        self.send_keys(OrderPageLocators.NAME_ORDER_INPUT, data["name"])
        self.send_keys(OrderPageLocators.SURNAME_ORDER_INPUT, data["surname"])
        self.send_keys(OrderPageLocators.ADRESS_ORDER_INPUT, data["address"])

        self.send_keys(OrderPageLocators.METRO_ORDER_INPUT, data["metro"])
        self.wait_and_click(OrderPageLocators.metro_option_by_name(data["metro"]))

        self.send_keys(OrderPageLocators.NUMBER_ORDER_INPUT, data["phone"])
        self.wait_and_click(OrderPageLocators.NEXT_ORDER_BUTTON)

        self.send_keys(OrderPageLocators.DATE_ORDER_INPUT, data["date_input"])
        self.wait_and_click(
            OrderPageLocators.calendar_date_by_label_part(data["date_label"])
        )

        self.wait_and_click(OrderPageLocators.RENT_TIME_DROPDOWN)
        self.wait_and_click(
            OrderPageLocators.rent_time_option_by_text(data["rent_time_text"])
        )

        self.wait_and_click(OrderPageLocators.ORDER_BUTTON)
        self.wait_and_click(OrderPageLocators.CONFIRM_BUTTON_IN_MODAL_WINDOW)
        return self.wait_and_find_element(OrderPageLocators.ORDER_BLOCK).text
    
    @allure.step("Кликнуть по лого Самоката")
    def open_scooter_main_page(self):
        self.wait_and_click(OrderPageLocators.SCOOTER_LOGO)