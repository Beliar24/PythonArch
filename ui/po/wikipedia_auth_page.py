import allure
from selenium.webdriver.common.by import By

from ui.config.base_page import BasePage


class WikipediaAuthLocators:
    THREE_DOTS = (By.XPATH, "//input[@id='p-personal-checkbox']")
    LOGIN = (By.XPATH, "//li/a[@accesskey='o']")
    USERNAME = (By.XPATH, "//input[@id='wpName1']")
    PASSWORD = (By.XPATH, "//input[@id='wpPassword1']")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='wpLoginAttempt']")
    GET_USERNAME = (By.XPATH, "//li[@id='pt-userpage-2']//span")


class WikipediaAuthActions(BasePage):

    @allure.step("Click on three dots button")
    def click_three_dots(self):
        self.find_element(WikipediaAuthLocators.THREE_DOTS).click()

    @allure.step("Click on login menu")
    def click_login_menu(self):
        self.find_element(WikipediaAuthLocators.LOGIN).click()

    @allure.step("Fill {username} and {password}")
    def auth(self, username, password):
        self.find_element(WikipediaAuthLocators.USERNAME).send_keys(username)
        self.find_element(WikipediaAuthLocators.PASSWORD).send_keys(password)
        self.find_element(WikipediaAuthLocators.LOGIN_BUTTON).click()

    @allure.step("Check user successfully auth")
    def get_auth_username(self):
        return self.find_element(WikipediaAuthLocators.GET_USERNAME).text
