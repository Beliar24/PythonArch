import allure
from appium.webdriver.common.appiumby import AppiumBy

from mobile.config.base_page import BasePage


class WikipediaSearchLocators:
    SKIP = (AppiumBy.XPATH, "//*[@text='SKIP']")
    SEARCH = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
    SEARCH_INPUT = (AppiumBy.XPATH, "//*[contains(@text,'Search Wikipedia')]")
    GET_TEXT = (AppiumBy.XPATH, "//*[@text='Automation for Apps']")


class SearchWikiPage(BasePage):

    @allure.step("Click on skip button")
    def click_skip(self):
        self.find_element(WikipediaSearchLocators.SKIP).click()

    @allure.step("Search world Appium")
    def search_appium_text(self):
        self.find_element(WikipediaSearchLocators.SEARCH).click()
        self.find_element(WikipediaSearchLocators.SEARCH_INPUT).send_keys("Appium")

    @allure.step("get founded world")
    def get_appium_article(self):
        return self.find_element(WikipediaSearchLocators.GET_TEXT).text
