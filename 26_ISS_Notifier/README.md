# 🚀 ISS Overhead Notifier

This Python script checks if the International Space Station (ISS) is currently flying over your location during the night and sends an email notification if both conditions are true.

## 📌 Features

- Checks ISS location using [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- Determines day/night using [Sunrise-Sunset API](https://sunrise-sunset.org/api)
- Sends email via Gmail SMTP when ISS is overhead during nighttime
- Runs continuously, checking every 60 seconds
