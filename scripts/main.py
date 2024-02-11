## Description
# This is a script to check the current time give the result about turning on or turning off the lights of office

import requests
from datetime import datetime
import pytz

# ilionx Office geographic coordinate
OFFICE_LAT = "50.930581"
OFFICE_LNG = "5.780691"

sunset_api_endpoint = "https://api.sunrise-sunset.org/json"
date_time_format = "%Y-%m-%dT%H:%M:%S+01:00"


def is_night():
    """
    Check if current time nighttime in the Amsterdam timezone based on sunrise and sunset data.
    Returns:
        bool: True if it's night, False otherwise.
    """
    try:
        location_parameters = {
            "lat": OFFICE_LAT,
            "lng": OFFICE_LNG,
            "formatted": "0",  # Formatted 0 helps to have time in 24h format, instead of having AM/PM format
            "tzid": "Europe/Amsterdam",
        }

        # Sending API request to sunrise=sunset website and fetch current day data
        response = requests.get(url=sunset_api_endpoint, params=location_parameters)
        response.raise_for_status()
        data = response.json()

        # Reading Sunrise and sunset time as string
        sunrise_string = data['results']['sunrise']
        sunset_string = data['results']['sunset']

        # Changing the type of parameters from string to datetime
        sunrise_formatted = datetime.strptime(sunrise_string, date_time_format)
        sunset_formatted = datetime.strptime(sunset_string, date_time_format)

        # Reading hour:min
        sunrise_time = sunrise_formatted.strftime("%H:%M")
        sunset_time = sunset_formatted.strftime("%H:%M")

        # Reading current time as hour:min with timezone of Amesterdam
        amsterdam_timezone = pytz.timezone('Europe/Amsterdam')
        time_now_str = datetime.now(amsterdam_timezone)
        current_time = time_now_str.strftime("%H:%M")

        if current_time >= sunset_time or current_time <= sunrise_time:
            return True
        else:
            return False
    except Exception as e:
        print(f"An unhandled error occurred: {e}")
        return False


if is_night():
    print("ON")
else:
    print("OFF")

