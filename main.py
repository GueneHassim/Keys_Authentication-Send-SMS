
CHIAVE = "9a3a8f14ce0fd8fd895ff845119262af"
OPEN_WEATHER_MAP_ENPOINT = "https://api.openweathermap.org/data/2.5/weather?"
MY_SENDING_NUMBER = "+13016913859"
MY_RECEIVING_NUMBER = "WRITE YOUR    PHONE NUMBER IN THIS SPACE"
AUCOUNT_SID_ = "AC14b819a94a7af51864305057264e999d"
AUTHTOKEN_ = "6e572cd4406eed458fe0a5efb8676c35"

import requests
import json
from twilio.rest import Client
import datetime
import time


#API endpoint paramters
paramters = {
    "lat": 50.598900,
    "lon": 5.512130,
    "appid": CHIAVE,
}

# API requests
response = requests.get(OPEN_WEATHER_MAP_ENPOINT, params=paramters)
status = response.raise_for_status
print(f"STATUS: {status}")

# Indexing the value of the response which I am interested in
data = response.json()
weather = data["weather"][0]
weather_id = weather["id"]
weather_main = weather["main"]
weather_description = weather["description"]
wind_speed = data["wind"]["speed"]

# Send the SMS
message_text = (f"Seraing BE actual weather update:\nweather id: {weather_id}\nweather main: {weather_main}\nweather description: {weather_description}\nwind speed: {wind_speed}")
def send_sms():
    client = Client(AUCOUNT_SID_, AUTHTOKEN_)
    message = client.messages.create(body=message_text, from_= MY_SENDING_NUMBER, to= MY_RECEIVING_NUMBER)

#now = datetime.datetime.now()
#hour = now.hour
#send_sms()

#program_on = True

#while program_on:
   # send_sms()
   # time.sleep(180)