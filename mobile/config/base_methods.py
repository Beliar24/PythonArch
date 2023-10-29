from mobile.config.base_page import BasePage


class BaseMethods(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, locator, time=10):
        return self._wait_element_located(locator, time)

    def find_button_element(self, locator, time=10):
        self._wait_element_clickable(locator, time)
        return self._wait_element_located(locator, time)

    def find_elements(self, locator, time=10):
        return self._wait_element_located(locator, time)