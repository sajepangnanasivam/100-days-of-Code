import requests
from datetime import datetime

MY_LAT = 60.035915
MY_LNG = 11.125331

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

# Response corresponding to our set location
data = response.json()

# Getting the 24h formatted Hour of the sunrise and sunset
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

