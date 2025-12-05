from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Config
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Подождать и найти все элементы")
    def wait_and_find_elements(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Подождать текст и найти элемент')
    def wait_text_and_find_element(self, locator, text):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    @allure.step('Подождать и кликнуть')
    def wait_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step('Подождать, прокрутить до видимости и кликнуть')
    def wait_and_click_element(self, element):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.element_to_be_clickable(element)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    
    @allure.step('Подождать и ввести текст')
    def send_keys(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step('Получить текущуюю ссылку')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключиться на новую вкладку')
    def switch_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(lambda d: d.current_url != "about:blank")
                break