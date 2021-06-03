from selenium.webdriver.common.by import By
from pom.decorators import element, with_webdriver
from selenium.webdriver.support.ui import Select
from pom.driver.driver import Driver
from pom.base import Base


class ParkingCostCalculator(Base):

    _parking_lot_dropdown_id = 'ParkingLot'
    _starting_date_input = (By.ID, 'StartingDate')
    _leaving_date_input = (By.ID, 'LeavingDate')
    _starting_time_input = (By.ID, 'StartingTime')
    _leaving_time_input = (By.ID, 'LeavingTime')
    _starting_time_am_radio = (By.XPATH, '//input[@id="StartingTime"]/following-sibling::input[@value="AM"]')
    _starting_time_pm_radio = (By.XPATH, '//input[@id="StartingTime"]/following-sibling::input[@value="PM"]')
    _leaving_time_am_radio = (By.XPATH, '//input[@id="LeavingTime"]/following-sibling::input[@value="AM"]')
    _leaving_time_pm_radio = (By.XPATH, '//input[@id="LeavingTime"]/following-sibling::input[@value="PM"]')
    _calculate_button = (By.NAME, 'Submit')
    _price_feedback_message = (By.CSS_SELECTOR, '*[class="SubHead"] b')
    _time_difference_message = (By.CSS_SELECTOR, 'span[class="BodyCopy"] b')

    @with_webdriver
    def __init__(self, driver):
        Base.__init__(self, driver)

    @property
    @element
    def starting_date_input(self):
        return self._starting_date_input

    @property
    @element
    def leaving_date_input(self):
        return self._leaving_date_input

    @property
    @element
    def starting_time_input(self):
        return self._starting_time_input

    @property
    @element
    def leaving_time_input(self):
        return self._leaving_time_input

    @property
    @element
    def starting_time_am_radio(self):
        return self._starting_time_am_radio

    @property
    @element
    def starting_time_pm_radio(self):
        return self._starting_time_pm_radio

    @property
    @element
    def leaving_time_am_radio(self):
        return self._leaving_time_am_radio

    @property
    @element
    def leaving_time_pm_radio(self):
        return self._leaving_time_pm_radio

    @property
    @element
    def calculate_button(self):
        return self._calculate_button

    @property
    @element
    def price_feedback_message(self):
        return self._price_feedback_message

    @property
    @element
    def time_difference_message(self):
        return self._time_difference_message

    def select_valet_parking(self):
        Select(Driver.driver.find_element_by_id(self._parking_lot_dropdown_id)).select_by_value('Valet')

    def select_short_term_parking(self):
        Select(Driver.driver.find_element_by_id(self._parking_lot_dropdown_id)).select_by_value('Short')

    def select_economy_parking(self):
        Select(Driver.driver.find_element_by_id(self._parking_lot_dropdown_id)).select_by_value('Economy')

    def select_long_term_garage_parking(self):
        Select(Driver.driver.find_element_by_id(self._parking_lot_dropdown_id)).select_by_value('Long-Garage')

    def select_long_term_surface_parking(self):
        Select(Driver.driver.find_element_by_id(self._parking_lot_dropdown_id)).select_by_value('Long-Surface')
