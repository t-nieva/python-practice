import requests
import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.header import Header

load_dotenv()

API_KEY = os.getenv("API_KEY_ALPHAVANTAGE")
API_KEY_NEWS = os.getenv("API_KEY_NEWSAPI")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

sender_email = os.getenv("GMAIL_EMAIL")
recipient_email = os.getenv("YAHOO_EMAIL")
password_app_gmail = os.getenv("PASSWORD_APP_GMAIL")

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()

time_series = data["Time Series (Daily)"]
dates = sorted(time_series.keys(), reverse=True)
yesterday = dates[0]
day_before_yesterday = dates[1]

close_yesterday = float(time_series[yesterday]["4. close"])
close_day_before = float(time_series[day_before_yesterday]["4. close"])

price_change = ((close_yesterday - close_day_before) / close_day_before) * 100
direction = "🔺" if price_change > 0 else "🔻"

if abs(price_change) >= 5:
    params_news = {
        "qInTitle": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "publishedAt",
        "apiKey": API_KEY_NEWS
    }

    response_news = requests.get(NEWS_ENDPOINT, params=params_news)
    data_news = response_news.json()

    articles = data_news.get("articles", [])[:3]
    print(articles)
    email_body = ''
    for article in articles:
        email_body += (f"\nHeadline: {article['title']}"
                       f"\nBrief: {article['description']}"
                       f"\nURL: {article['url']}\n\n")

    subject = f"{STOCK} Stock Alert"
    body = f"Stock Alert: {direction}{price_change:.2f}%\n{email_body}"
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender_email
    msg["To"] = recipient_email

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password_app_gmail)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=msg.as_string()
        )
else:
    print("No significant change")
