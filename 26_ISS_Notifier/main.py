import requests
import datetime as dt
import smtplib
import time

YAHOO_EMAIL = "test@yahoo.com"
GMAIL_EMAIL = "test@gmail.com"
PASSWORD_APP_GMAIL = "your_pass"

MY_LAT = 42.69194657754181
MY_LNG = 23.337434682448595

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    # My position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted":0
    }

    response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()['results']
    sunset_hour = int(data['sunset'].split("T")[1].split(":")[0])
    sunrise_hour = int(data['sunrise'].split("T")[1].split(":")[0])

    now = dt.datetime.now()
    now_hour = now.hour

    if now_hour >= sunset_hour or now_hour <= sunrise_hour:
        return True
    else:
        return False

sender_email = GMAIL_EMAIL
recipient_email = YAHOO_EMAIL

while True:
    # Run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=PASSWORD_APP_GMAIL)
            connection.sendmail(from_addr=sender_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:ISS is close\n\nLook up! The ISS is above you in the sky.")
