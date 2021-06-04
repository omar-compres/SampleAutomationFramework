from pom.factory import Factory
from pom.constants.contants import expected_values
import time


class TestNegativePath:

    def test_negative_time_difference(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("05:59")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['negative_difference'],
                                           page.price_feedback_message.text)

    def test_invalid_character_on_starting_date(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("k")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['incorrect_date_value'],
                                           page.price_feedback_message.text)

    def test_invalid_character_on_ending_date(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("k")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['incorrect_date_value'],
                                           page.price_feedback_message.text)

    def test_invalid_character_on_starting_time(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("z")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['incorrect_time_value'],
                                           page.price_feedback_message.text)

    def test_invalid_character_on_ending_time(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("z")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['incorrect_time_value'],
                                           page.price_feedback_message.text)

    def test_default_values_on_page_load(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['incorrect_date_value'],
                                           page.price_feedback_message.text)

    def test_past_dates(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("5/10/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("5/11/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['past_dates-error_message'],
                                           page.price_feedback_message.text)

    def test_for_non_existent_dates(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("5/10/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("5/11/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['past_dates-error_message'],
                                           page.price_feedback_message.text)
