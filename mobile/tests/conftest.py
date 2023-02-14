import pytest
from appium import webdriver

from mobile.config.capabilities import caps
from mobile.utils.read_property import get_property


@pytest.fixture(scope="function")
def appium():
    driver = webdriver.Remote(get_property("url"), caps())
    yield driver
    driver.quit()
