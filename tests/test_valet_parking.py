from pom.factory import Factory
from pom.constants.contants import expected_values


class TestValetParking:

    def test_few_minutes_difference(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:02")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['valet_less_than_5_hours'], page.price_feedback_message.text)

    def test_few_hours_less_than_5(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("10:59")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['valet_less_than_5_hours'], page.price_feedback_message.text)

    def test_for_slightly_over_5_hours(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("11:15")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['valet_over_5_less_than_24'],
                                           page.price_feedback_message.text)

    def test_for_slightly_under_24_hours(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/29/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("05:59")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['valet_over_5_less_than_24'],
                                           page.price_feedback_message.text)

    def test_for_a_couple_of_days(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.starting_date_input.send_keys("6/29/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("7/06/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['valet_7_days_price'],
                                           page.price_feedback_message.text)

