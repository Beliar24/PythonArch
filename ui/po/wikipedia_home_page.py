import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from ui.config.base_page import BasePage


class WikipediaLocators:
    WELCOME = (By.XPATH, "//span[@id='Welcome_to_Wikipedia']")
    SEARCH = (By.XPATH, "//input[@name='search']")
    SEARCH_RESULT = (By.XPATH, "//h1[@id='firstHeading']")


class WikipediaActions(BasePage):

    @allure.step("Get text when opened the site")
    def get_text_when_come(self):
        welcome = self.find_element(WikipediaLocators.WELCOME)
        return welcome.text

    @allure.step("Type in search {text}")
    def search_text(self, text):
        search = self.find_element(WikipediaLocators.SEARCH)
        search.send_keys(text)
        search.send_keys(Keys.ENTER)

    @allure.step("Check searched text")
    def get_text_search_result(self):
        found = self.find_element(WikipediaLocators.SEARCH_RESULT)
        return found.text

