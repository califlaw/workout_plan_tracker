import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


week = input("Week: ")
exercise = input("Exercise: ")
weight = input("Weight: ")
sets = input("Sets: ")
reps = input("Reps: ")
day = datetime.today()
today = day.strftime("%d-%m-%Y")

sheety_endpoint = f"https://api.sheety.co/{os.environ.get('ID')}/myWorkouts/workouts"

headers = {
    'AUTHORIZATION': os.environ.get("TOKEN")
}

params = {
    "workout": {
        'week': week,
        'exercise': exercise,
        'weight': weight,
        'sets': sets,
        'reps': reps,
        'date': today
    }
}

response = requests.post(url=sheety_endpoint, json=params, headers=headers)

