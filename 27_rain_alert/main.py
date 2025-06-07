# Plan to run this script periodically in the future using cron (Linux/macOS)
# For example, to run daily at 7 AM or every 3 hours.

import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("GMAIL_EMAIL")
recipient_email = os.getenv("YAHOO_EMAIL")
api_key = os.getenv("OWM_API_KEY")
password_app_gmail = os.getenv("PASSWORD_APP_GMAIL")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 42.69785084321178,
    "lon": 23.342283430659762,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for forecast in weather_data['list']:
    weather_id = forecast['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True
        break

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password_app_gmail)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:Weather\n\nIt's going to rain today. Remember to bring an umbrella.")
