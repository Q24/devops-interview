import requests
from datetime import datetime,timedelta
import pytz
 
#Set IllionX office coordinates
latitude = 28.262222
longitude = -96.747165
 
#Request to API
url = "https://api.sunrise-sunset.org/json"
params = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0,
        "date": "today",
        }
 
input_format   = "%Y-%m-%dT%H:%M:%S+00:00"
output_format  = "%H:%M:%S"

#API Response
resp_json = requests.get(url, params=params).json()
# print(resp_json)
sunrise_date_time  = resp_json["results"]["sunrise"]
sunset_date_time  = resp_json["results"]["sunset"]

sunrise = datetime.strptime(sunrise_date_time, input_format)
sunset = datetime.strptime(sunset_date_time, input_format)

#Convert sunrise and sunset times to CET timezone
sunrise_cet = sunrise.astimezone(pytz.timezone('CET'))
sunset_cet = sunset.astimezone(pytz.timezone('CET'))

# Convert it to CET
now_cet = datetime.now(pytz.timezone('CET'))
# print("CET time:", now_cet)

#Check if lights must be ON or OFF
if now_cet < sunrise_cet:
    print(f"ON")
elif sunrise_cet < now_cet < sunset_cet:
    print(f"OFF")
else:
    print(f"ON")
