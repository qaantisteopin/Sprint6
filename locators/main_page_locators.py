from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "div.accordion__item div.accordion__button")
    FAQ_ANSWERS = [(By.ID, "accordion__panel-0"), (By.ID, "accordion__panel-1"), (By.ID, "accordion__panel-2"), (By.ID, "accordion__panel-3"), (By.ID, "accordion__panel-4"), (By.ID, "accordion__panel-5"), (By.ID, "accordion__panel-6"), (By.ID, "accordion__panel-7")]
    HEADER_ORDER_BUTTON = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    MIDDLE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    ORDER_HEADER_FORM=(By.CSS_SELECTOR, "Order_Header__BZXOb")
    METRO_OPTION = (By.XPATH, "//div[contains(text(), 'Бульвар Рокоссовского')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
