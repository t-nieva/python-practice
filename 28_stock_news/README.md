# Stock News Email Alert

This project monitors the daily closing price of a stock (default: Tesla Inc, TSLA). 
If the price changes by 5% or more compared to the previous day, 
it fetches the latest news articles about the company and sends an email alert 
with the news headlines and summaries.

## Features

- Fetches daily stock price data from Alpha Vantage.
- Detects significant price changes (≥5%).
- Retrieves top 3 news articles from NewsAPI if a significant change is detected.
- Sends an email alert with the price change and news summaries.

**Set up environment variables** in a `.env` file:
   ```
   API_KEY_ALPHAVANTAGE=your_alphavantage_api_key
   API_KEY_NEWSAPI=your_newsapi_key
   GMAIL_EMAIL=your_gmail_address
   YAHOO_EMAIL=recipient_email_address
   PASSWORD_APP_GMAIL=your_gmail_app_password
   ```

## How it works

- The script checks the closing prices for the last two days.
- If the price change is 5% or more, it fetches the latest news and sends an email.
- If not, it prints "No significant change".
