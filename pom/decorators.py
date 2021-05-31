from pom.driver.driver import Driver
from pom.element import Element
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def with_webdriver(original_func):
    def wrapper(self, *args, **kwargs):
        return original_func(self, Driver.driver, *args, **kwargs)
    return wrapper


def element(original_func):
    def wrapper(*args, **kwargs):
        _element = WebDriverWait(Driver.driver, 30).until(
            expected_conditions.visibility_of_element_located(
                original_func(*args, **kwargs)))
        return Element(_element, original_func(*args, **kwargs))
    return wrapper
