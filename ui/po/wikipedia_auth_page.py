import allure
from selenium.webdriver.common.by import By

from ui.config.base_methods import BaseMethods


class WikipediaAuthActions(BaseMethods):

    __THREE_DOTS = (By.XPATH, "//input[@id='p-personal-checkbox']")
    __LOGIN = (By.XPATH, "//li/a[@accesskey='o']")
    __USERNAME = (By.XPATH, "//input[@id='wpName1']")
    __PASSWORD = (By.XPATH, "//input[@id='wpPassword1']")
    __LOGIN_BUTTON = (By.XPATH, "//button[@id='wpLoginAttempt']")
    __GET_USERNAME = (By.XPATH, "//li[@id='pt-userpage-2']//span")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on three dots button")
    def click_three_dots(self):
        self.find_element(self.__THREE_DOTS).click()
        return WikipediaAuthActions

    @allure.step("Click on login menu")
    def click_login_menu(self):
        self.find_element(self.__LOGIN).click()
        return WikipediaAuthActions

    @allure.step("Fill {username} and {password}")
    def auth(self, username, password):
        self.find_element(self.__USERNAME).send_keys(username)
        self.find_element(self.__PASSWORD).send_keys(password)
        self.find_element(self.__LOGIN_BUTTON).click()
        return WikipediaAuthActions

    @allure.step("Check user successfully auth")
    def get_auth_username(self):
        return self.find_element(self.__GET_USERNAME).text
