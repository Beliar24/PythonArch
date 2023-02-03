import allure

from ui.po.wikipedia_auth_page import WikipediaAuthActions
from ui.po.wikipedia_home_page import WikipediaActions
from ui.utils import read_property


@allure.description("Open site wikipedia and check correct welcome text")
def test_wikipedia_search(browser):
    welcome = WikipediaActions(browser)
    welcome.open_page()

    assert "Welcome to Wikipedia" in welcome.get_text_when_come()


@allure.description("Open site wikipedia and search appium")
def test_search_appium_info(browser):
    search = WikipediaActions(browser)
    search.open_page()
    search.search_text("Appium")

    assert "Search result" in search.get_text_search_result()


@allure.description("Auth with user")
def test_go_to_account(auth):
    auth = WikipediaAuthActions(auth)

    assert read_property.get_property("username") in auth.get_auth_username()
