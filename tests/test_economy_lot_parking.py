from pom.factory import Factory
from pom.constants.contants import expected_values


class TestEconomyLotParking:

    def test_few_minutes_difference(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_long_term_surface_parking()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:02")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['economy_hourly_price'],
                                           page.price_feedback_message.text)

    def test_for_slightly_under_two_hours(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_long_term_surface_parking()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:59")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['economy_1.5_hours'], page.price_feedback_message.text)

    def test_daily_max(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_long_term_surface_parking()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("11:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['economy_5_hours'],
                                           page.price_feedback_message.text)

    def test_for_weekly_limits(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_long_term_surface_parking()
        page.starting_date_input.send_keys("7/01/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("7/07/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['economy_6_days_1_hour'],
                                           page.price_feedback_message.text)
        page.get()
        page.select_long_term_surface_parking()
        page.starting_date_input.send_keys("7/01/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("7/08/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['economy_7_days'],
                                           page.price_feedback_message.text)

    def test_for_two_weeks(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_long_term_surface_parking()
        page.starting_date_input.send_keys("7/01/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("7/15/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['economy_2_weeks'],
                                           page.price_feedback_message.text)
