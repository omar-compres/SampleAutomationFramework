from selenium.webdriver.common.by import By
from pom.decorators import element, with_webdriver
from selenium.webdriver.support.ui import Select
from pom.constants.expected_values import urls


class ParkingCostCalculator:

    @with_webdriver
    def __init__(self, driver):
        self.driver = driver

    _parking_lot_dropdown = (By.ID, 'ParkingLot')

    @property
    @element
    def parking_lot_dropdown(self):
        return self._parking_lot_dropdown

    @with_webdriver
    def get(self, driver, url=urls['ParkingCostCalculator']):
        driver.get(url)

    def select_valet_parking(self):
        Select(self.parking_lot_dropdown).select_by_value('Valet')

    def select_short_term_parking(self):
        Select(self.parking_lot_dropdown).select_by_value('Short')

    def select_economy_parking(self):
        Select(self.parking_lot_dropdown).select_by_value('Economy')

    def select_long_term_garage_parking(self):
        Select(self.parking_lot_dropdown).select_by_value('Long-Garage')

    def select_long_term_surface_parking(self):
        Select(self.parking_lot_dropdown).select_by_value('Long-Surface')



