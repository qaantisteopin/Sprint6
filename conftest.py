import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Edge()
    browser.get(Urls.MESTO_URL)
    yield browser
    browser.quit()