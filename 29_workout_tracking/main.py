from dotenv import load_dotenv
import os
import requests
import datetime as dt

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY_NUTRITIONIX")
API_ID = os.getenv("APP_ID_NUTRITIONIX")
MY_SHEET = os.getenv("MY_SHEET")
AUTHORIZATION_BASIC=os.getenv("AUTHORIZATION_BASIC_SHEET")

# User profile
USER_PROFILE = {
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 158,
    "age": 32
}

# Endpoints
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/{MY_SHEET}"

# Headers
nutritionix_headers = {
    'Content-Type': 'application/json',
    'x-app-id':API_ID,
    'x-app-key':API_KEY
}

sheety_headers = {
    'Authorization':f'Basic {AUTHORIZATION_BASIC}'
}

# Nutritionix API
def post_exercise_data(query):
    payload = {**USER_PROFILE, "query": query}
    response = requests.post(url=NUTRITIONIX_ENDPOINT, json=payload, headers=nutritionix_headers)
    return response.json()['exercises']

# Add exercise data to Sheety
def log_exercise_to_sheet(exercises):
    for res in exercises:
        now = dt.datetime.now()
        sheety_format_data = now.strftime("%d/%m/%Y")
        time = str(now).split(" ")[1].split(".")[0]
        exercise = res['name'].capitalize()
        duration_min = res['duration_min']
        calories = res['nf_calories']
        payloads = {
            "лист1": {
                'date': sheety_format_data,
                'time': time,
                'exercise': exercise,
                'duration': duration_min,
                'calories': calories,
            }
          }
        response = requests.post(url=SHEETY_ENDPOINT, json=payloads, headers=sheety_headers)
        print(response.json())

# Retrieve existing entries from the sheet
def retrieve_logged_exercises():
    response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
    data = response.json()
    print(data)
    return data

# Exercise text example: "run for 2 hour"
exercise_text = input("Tell me which exercises you did: ")
list_results = post_exercise_data(exercise_text)
log_exercise_to_sheet(list_results)
retrieve_logged_exercises()
