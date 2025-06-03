import smtplib
import datetime as dt
import random
import pandas

YAHOO_EMAIL = "test@yahoo.com"
GMAIL_EMAIL = "test@gmail.com"
PASSWORD_APP_GMAIL = "your_pass"

sender_email = GMAIL_EMAIL
recipient_email = YAHOO_EMAIL

now = dt.datetime.now()
birthday = dt.datetime(year=2025, month=6, day=2)

today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    name = birthdays_dict[today]["name"]
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", mode="r", encoding="utf-8") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=PASSWORD_APP_GMAIL)
        connection.sendmail(from_addr=sender_email,
                        to_addrs=recipient_email,
                        msg=f"Subject:Happy Birthday\n\n{letter}")
