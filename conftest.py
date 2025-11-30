import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver(request):
    browser = webdriver.Chrome()
    browser.get(Urls.MESTO_URL)
    yield browser
    browser.quit()