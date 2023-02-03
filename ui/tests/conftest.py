import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from ui.po.wikipedia_auth_page import WikipediaAuthActions
from ui.utils import read_property


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def auth(browser):
    go = WikipediaAuthActions(browser)
    go.open_page()
    go.click_three_dots()
    go.click_login_menu()
    go.auth(read_property.get_property("username"), read_property.get_property("password"))
    yield browser
