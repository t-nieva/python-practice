# Cheap Flight Finder ✈️

**Cheap Flight Finder** is a Python project that automatically searches for the cheapest flights 
to your chosen destinations and notifies you about great deals via Telegram.

## Features

- Searches for the cheapest flights based on data from a Google Sheet.
- Updates IATA codes for cities in your Google Sheet.
- Sends Telegram notifications if a flight is found below your target price.
- Integrates with the Amadeus API for flight search.

## Required Environment Variables

Create a `.env` file in the project root and add the following variables:

```
SHEETY_BASIC_AUTH=your_sheety_basic_auth
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```


## How It Works

1. The script fetches a list of cities and prices from your Google Sheet.
2. It updates missing IATA codes for each city.
3. It searches for the cheapest flights for the next 6 months.
4. If a flight is found below your target price, it sends a Telegram notification.

**Author:**  
https://github.com/t-nieva
