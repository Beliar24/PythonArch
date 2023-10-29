import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from ui.config.base_methods import BaseMethods


class WikipediaActions(BaseMethods):
    __WELCOME = (By.XPATH, "//span[@id='Welcome_to_Wikipedia']")
    __SEARCH = (By.XPATH, "//input[@name='search']")
    __SEARCH_RESULT = (By.XPATH, "//h1[@id='firstHeading']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get text when opened the site")
    def get_text_when_come(self):
        welcome = self.find_element(self.__WELCOME)
        return welcome.text

    @allure.step("Type in search {text}")
    def search_text(self, text):
        search = self.find_element(self.__SEARCH)
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        return WikipediaActions

    @allure.step("Check searched text")
    def get_text_search_result(self):
        found = self.find_element(self.__SEARCH_RESULT)
        return found.text
