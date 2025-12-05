from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderPageData, Urls
import allure
import pytest  

class TestOrderPage:

    @pytest.mark.parametrize("order", OrderPageData.VALID_ORDERS)
    @allure.title('Проверка формы заказа самоката')
    @allure.description('Принимаем куки, открываем форму заказа через кнопку в шапке, заполняем первую половину формы, переходим на вторую половину формы, заполняем вторую половину формы, оформляем заказ, проверяем наличие Номера заказа в модальном окне')
    def test_scooter_order_form(self, driver, order):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.open_header_scooter_order_form()
        order_page = OrderPage(driver)
        text = order_page.fill_order_form(order)
        assert 'Номер заказа' in text, 'Текст с номером заказа не найден'
    
    @allure.title('Проверка перехода на основную страницу')
    @allure.description('Принимаем куки, открываем форму заказа через кнопку на странице, кликаем по логотипу Самоката, сравниваем URL')
    def test_open_main_page_from_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.open_middle_button_scooter_order_form()
        order_page = OrderPage(driver)
        order_page.open_scooter_main_page()
        current_url = main_page.get_current_url()
        assert current_url == Urls.MESTO_URL