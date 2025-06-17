import logging
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight

# ==================== Logging Setup ====================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================
for data in sheet_data:
    if not data["iataCode"]:
        data["iataCode"] = flight_search.get_destination_code(data["city"])

data_manager.destination_data = sheet_data
data_manager.update_codes()

# ==================== Search for Flights ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for data in sheet_data:
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        data["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < data["lowestPrice"]:
        logging.info(f"Lower price flight found to {data['city']}!")
        notification_manager.send_message(
            f"✈️ <b>Low price alert!</b>\n"
            f"Only £{cheapest_flight.price} to fly from {ORIGIN_CITY_IATA} "
            f"to {cheapest_flight.destination_airport}.\n"
            f"From: {cheapest_flight.out_date} ✈️ To: {cheapest_flight.return_date}"
        )
