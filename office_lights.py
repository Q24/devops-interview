import requests
from datetime import datetime, timedelta
import pytz

# IllionX Office Coordinates
latitude = 50.930581
longitude = 5.780691

# Get the sunset and sunrise times from the API
response = requests.get(f"https://api.sunrise-senset.org/json?lat={latitude}&lng={longitude}&formatted=0")
data = response.json()

cet = pytz.timezone('CET') # Setting times to CET timezone
sunrise = sunrise.astimezone(cet)
sunset = sunset.astimezone(cet)

now = datetime.now(cet) # Current time

if sunrise < now < sunset:
  print('OFF')
else:
  print('ON')

