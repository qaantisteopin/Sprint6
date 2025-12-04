from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "div.accordion__item div.accordion__button")
    FAQ_ANSWERS = [(By.ID, "accordion__panel-0"), (By.ID, "accordion__panel-1"), (By.ID, "accordion__panel-2"), (By.ID, "accordion__panel-3"), (By.ID, "accordion__panel-4"), (By.ID, "accordion__panel-5"), (By.ID, "accordion__panel-6"), (By.ID, "accordion__panel-7")]
    HEADER_ORDER_BUTTON = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    MIDDLE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    ORDER_HEADER_FORM=(By.CSS_SELECTOR, "Order_Header__BZXOb")
    NAME_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Фамилия']")
    ADRESS_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Станция метро']")
    NUMBER_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_ORDER_BUTTON=(By.XPATH, "//button[text()='Далее']")
    DATE_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_DROPDOWN=(By.XPATH, "//div[@class='Dropdown-control' and @aria-haspopup='listbox']")
    DROPDOWN_ELEMENT=(By.XPATH, "//div[@role='option' and text()='сутки']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_BUTTON_IN_MODAL_WINDOW = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    METRO_OPTION = (By.XPATH, "//div[contains(text(), 'Бульвар Рокоссовского')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    CALENDAR_DATE_BUTTON = (By.XPATH, "//div[contains(@aria-label, 'Choose пятница, 5-е декабря')]")
    ORDER_BLOCK = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi') and contains(text(), 'Номер заказа')]")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    TRACK_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть заказ']")

