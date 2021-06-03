from pom.decorators import with_webdriver
from pom.constants.contants import urls


class Base:

    def __init__(self, driver):
        self.driver = driver

    base_url = urls["ParkingCostCalculator"]

    @with_webdriver
    def get(self, driver, url=base_url):
        driver.get(url)
