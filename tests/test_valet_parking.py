from pom.constants.contants import urls
from pom.pageobjects.parking_cost_calculator import ParkingCostCalculator
from pom.driver.driver import Driver

import time


class TestValetParking:

    def test_sample_script(self):

        parking_cost_calculator = ParkingCostCalculator(Driver.driver)
        parking_cost_calculator.get()







