from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pom.driver.driver import Driver


class Element(object):

    element = None
    locator = None

    def __init__(self, element, locator):
        self.element = element
        self.locator = locator

    @property
    def text(self):
        return self.element.text

    def is_displayed(self):
        return self.element.is_displayed()

    def send_keys(self, value):
        self.element.clear()
        self.element.send_keys(value)

    def click(self):
        try:
            self.element.click()
        except TimeoutException:
            print("Web element locator {} exception: ".format(
                self.locator) + TimeoutException)

    def wait_for_element(self):
        try:
            WebDriverWait(Driver.driver, 15).until(ec.visibility_of(self.element))
        except TimeoutException:
            print("Web element locator {} exception: ".format(
                self.locator) + TimeoutException)

    def get_attribute(self, attribute):
        return self.element.get_attribute(attribute)
