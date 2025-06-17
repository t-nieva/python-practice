import os
import requests
import logging

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
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
