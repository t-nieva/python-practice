from dotenv import load_dotenv
import os
import requests
import logging

load_dotenv()
SHEETY_BASIC_AUTH = os.getenv("SHEETY_BASIC_AUTH")
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

sheety_headers = {
    'Authorization': f'Basic {SHEETY_BASIC_AUTH}'
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
            response.raise_for_status()
            data = response.json()
            self.destination_data = data.get("prices", [])

            if not self.destination_data:
                logging.warning("No destination data found in Google Sheet.")

            return self.destination_data
        except requests.RequestException as e:
            logging.error(f"Failed to get destination data: {e}")
            return []

    def update_codes(self):
        for data in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": data["iataCode"]
                }
            }

            try:
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{data['id']}",
                    json=new_data,
                    headers=sheety_headers)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"Failed to update IATA code for {data['city']}: {e}")

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        print(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data
