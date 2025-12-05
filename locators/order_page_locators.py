from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Фамилия']")
    ADRESS_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Станция метро']")
    NUMBER_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_ORDER_BUTTON=(By.XPATH, "//button[text()='Далее']")
    DATE_ORDER_INPUT=(By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_DROPDOWN=(By.XPATH, "//div[@class='Dropdown-control' and @aria-haspopup='listbox']")
    DROPDOWN_ELEMENT=(By.XPATH, "//div[@role='option' and text()='сутки']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_BUTTON_IN_MODAL_WINDOW = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    TRACK_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть заказ']")
    CALENDAR_DATE_BUTTON = (By.XPATH, "//div[contains(@aria-label, 'Choose пятница, 5-е декабря')]")
    ORDER_BLOCK = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi') and contains(text(), 'Номер заказа')]")
    METRO_OPTION = (By.XPATH, "//div[contains(text(), 'Бульвар Рокоссовского')]")

    @staticmethod
    def metro_option_by_name(metro_name: str):
        return (
            By.XPATH,
            f"//div[contains(text(), '{metro_name}')]",
        )
    
    @staticmethod
    def rent_time_option_by_text(text: str):
        return (
            By.XPATH,
            f"//div[@role='option' and text()='{text}']",
        )
    
    @staticmethod
    def calendar_date_by_label_part(label_part: str):
        return (
            By.XPATH,
            f"//div[contains(@aria-label, 'Choose {label_part}')]",
        )