from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "div.accordion__item div.accordion__button")
    FAQ_ANSWERS = [(By.ID, "accordion__panel-0"), (By.ID, "accordion__panel-1"), (By.ID, "accordion__panel-2"), (By.ID, "accordion__panel-3"), (By.ID, "accordion__panel-4"), (By.ID, "accordion__panel-5"), (By.ID, "accordion__panel-6"), (By.ID, "accordion__panel-7")]