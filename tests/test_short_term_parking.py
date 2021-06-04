from pom.factory import Factory
from pom.constants.contants import expected_values
import allure


class TestShortTermParking:

    @allure.title("Validating minimum rate with a few minutes.")
    def test_few_minutes_difference(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_short_term_parking()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:02")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['short_less_than_1_hour'], page.price_feedback_message.text)

    @allure.title("Validating minimum rate with 1 hour and 59 minutes.")
    def test_for_slightly_under_two_hours(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_short_term_parking()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:59")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['short_slightly_less_than_2'], page.price_feedback_message.text)

    @allure.title("Validating daily limit with 13 hours.")
    def test_daily_max(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_short_term_parking()
        page.starting_date_input.send_keys("6/30/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_pm_radio.click()
        page.leaving_time_input.send_keys("07:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['short_daily_max'],
                                           page.price_feedback_message.text)

    @allure.title("Validating daily limit plus additional time")
    def test_for_slightly_over_24_hours(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_short_term_parking()
        page.starting_date_input.send_keys("6/29/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("6/30/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("07:30")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['short_daily_plus_1.5_hours'],
                                           page.price_feedback_message.text)

    @allure.title("Validating daily limit with 3 days.")
    def test_for_a_couple_of_days(self):
        page = Factory.parking_cost_calculator
        page.get()
        page.select_short_term_parking()
        page.starting_date_input.send_keys("7/01/2021")
        page.starting_time_am_radio.click()
        page.starting_time_input.send_keys("06:00")
        page.leaving_date_input.send_keys("7/04/2021")
        page.leaving_time_am_radio.click()
        page.leaving_time_input.send_keys("06:00")
        page.calculate_button.click()
        assert Factory.utils.is_text_equal(expected_values['short_three_days_price'],
                                           page.price_feedback_message.text)
