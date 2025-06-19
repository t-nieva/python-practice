import os
import requests
import smtplib
import logging
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.smtp_address = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.email = os.getenv("MY_EMAIL")
        self.email_password = os.getenv("MY_EMAIL_PASSWORD")

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()
            logging.info("Notification sent successfully.")
        except requests.RequestException as e:
            logging.error(f"Failed to send notification: {e}")

    def send_emails(self, email_list, email_body):
        """Sends emails to a list of recipients."""
        try:
            with smtplib.SMTP(self.smtp_address) as connection:
                connection.starttls()
                connection.login(self.email, self.email_password)
                for email in email_list:
                    connection.sendmail(
                        from_addr=self.email,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                    )
            logging.info("Email notifications sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send email notifications: {e}")
