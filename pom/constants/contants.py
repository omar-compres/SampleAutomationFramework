urls = {
    "ParkingCostCalculator": "https://www.shino.de/parkcalc/"
}

expected_values = {
    "negative_difference": "ERROR! YOUR LEAVING DATE OR TIME IS BEFORE YOUR STARTING DATE OR TIME",
    "incorrect_date_value": "ERROR! ENTER A CORRECTLY FORMATTED DATE",
    "incorrect_time_value": "ERROR! UNEXPECTED TIME VALUE. PLEASE MAKE SURE TO USE THIS FORMAT: {HH:MM}",
    "past_dates-error_message": "ERROR! PAST DATES ARE NOT ACCEPTED",

    "valet_less_than_5_hours": "$ 12.00",
    "valet_over_5_less_than_24": "$ 18.00",
    "valet_7_days_price": "$ 126.00",

    "short_less_than_1_hour": "$ 2.00",
    "short_slightly_less_than_2": "$ 4.00",
    "short_daily_max": "$ 24.00",
    "short_daily_plus_1.5_hours": "$ 27.00",
    "short_three_days_price": "$ 72.00",

    "long_term_garage_hourly_price": "$ 2.00",
    "long_term_garage_1.5_hours": "$ 4.00",
    "long_term_garage_7_hours": "$ 12.00",
    "long_term_garage_6_days_1_hour": "$ 72.00",
    "long_term_garage_7_days": "$ 72.00",
    "long_term_garage_2_weeks": "$ 144.00",

    "long_term_surface_hourly_price": "$ 2.00",
    "long_term_surface_1.5_hours": "$ 4.00",
    "long_term_surface_6_hours": "$ 10.00",
    "long_term_surface_6_days_1_hour": "$ 60.00",
    "long_term_surface_7_days": "$ 60.00",
    "long_term_surface_2_weeks": "$ 120.00",

    "economy_hourly_price": "$ 2.00",
    "economy_1.5_hours": "$ 4.00",
    "economy_5_hours": "$ 9.00",
    "economy_6_days_1_hour": "$ 54.00",
    "economy_7_days": "$ 54.00",
    "economy_2_weeks": "$ 108.00"

}
