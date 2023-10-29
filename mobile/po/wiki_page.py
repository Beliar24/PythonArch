import allure
from appium.webdriver.common.appiumby import AppiumBy

from mobile.config.base_methods import BaseMethods


class SearchWikiPage(BaseMethods):

    __SKIP = (AppiumBy.XPATH, "//*[@text='SKIP']")
    __SEARCH = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
    __SEARCH_INPUT = (AppiumBy.XPATH, "//*[contains(@text,'Search Wikipedia')]")
    __GET_TEXT = (AppiumBy.XPATH, "//*[@text='Automation for Apps']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on skip button")
    def click_skip(self):
        self.find_element(self.__SKIP).click()
        return SearchWikiPage

    @allure.step("Search world Appium")
    def search_appium_text(self):
        self.find_element(self.__SEARCH).click()
        self.find_element(self.__SEARCH_INPUT).send_keys("Appium")
        return SearchWikiPage

    @allure.step("get founded world")
    def get_appium_article(self):
        return self.find_element(self.__GET_TEXT).text
