import allure

from mobile.po.wiki_page import SearchWikiPage


@allure.description("This test is searching word Appium and compare with pre-pared phrase")
def test_search_text(appium):
    search = SearchWikiPage(appium)

    search.click_skip()
    search.search_appium_text()

    assert "Automation for Apps" in search.get_appium_article()
