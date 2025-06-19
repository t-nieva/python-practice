# ✈️ Cheap Flight Finder
A Python script that helps you find the cheapest flights from your origin city using the Amadeus API 
and sends notifications via Telegram and email when better prices are found.

## 🔍 Features
+ Fetches destinations and target prices from Google Sheets
+ Fills in missing IATA codes for destinations
+ Searches for direct flights from a defined origin
+ If no direct flights found → searches for flights with 1 or 2 stopovers 
+ Compares prices to those in the sheet
+ Sends alerts:
  + 💬 via Telegram 
  + 📧 via Email to subscribed users

## 📦 Technologies Used
- Python 3
- Amadeus Flight Offers Search API
- Google Sheets API (via Sheety or your own integration)
- SMTP for sending emails 
- Telegram Bot API

## 🗂 Project Structure
```commandline   
├── main.py                  # Main flight search + notification logic
├── flight_search.py         # Handles API calls to Amadeus
├── flight_data.py           # Picks the cheapest flight from returned results
├── data_manager.py          # Connects with Google Sheet for destinations/emails
├── notification_manager.py  # Sends notifications (Telegram and Email)
├── .env                     # Environment variables (not committed)
└── README.md                # This file
```

## 🔐 .env File Example
Create a .env file in the project root with the following:

### Telegram bot credentials
TELEGRAM_BOT_TOKEN=your_bot_token

TELEGRAM_CHAT_ID=your_chat_id

### Email credentials
EMAIL_PROVIDER_SMTP_ADDRESS=smtp.gmail.com

MY_EMAIL=your_email@gmail.com

MY_EMAIL_PASSWORD=your_email_app_password

## 🛠 Setup Instructions
- Clone this repository
- Set up your .env file as shown above
- Make sure your Google Sheet contains the following columns: city, iataCode, lowestPrice, whatIsYourEmail?
- Get access to the Amadeus API:
  - Register at https://developers.amadeus.com
  - Create an application and retrieve your credentials
  - Use those to obtain an access token in FlightSearch

## 🚀 How to Run
python main.py

⚠️ The script adds a 2-second delay between API calls to avoid hitting Amadeus rate limits.

## 📧 Notifications
If a cheaper flight is found than the current lowest price:
- A Telegram message is sent to the configured chat 
- An Email is sent to all customers listed in the Google Sheet

## 📝 Sample Message
✈️ Low price alert!
Only GBP 75 to fly direct from LON to BER,
departing on 2025-07-15 and returning on 2025-07-22.

## 💡 Notes
Low-cost airlines may not appear in the free tier of the Amadeus API

Not all carriers (e.g., American Airlines, Delta) are supported in test mode

This script supports both direct and indirect flights (up to 2 stopovers)

## 📬 Feedback
This is a learning project. If you find bugs or want to contribute, feel free to open an issue or reach out. 🙌

**Author:**  
https://github.com/t-nieva
