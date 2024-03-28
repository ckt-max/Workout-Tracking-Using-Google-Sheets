import requests
import os
import datetime as dt

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': os.getenv('NUTRI_APP_ID') ,
    'x-app-key': os.getenv('NUTRI_APP_KEY'),
    'Content-Type': 'application/json',
}

query = input("What did you do today?")
params = {
    "query": query,
}

response = requests.post(url=exercise_endpoint,json=params, headers=headers)
exercise_list = response.json()['exercises']

# putting data in the sheet
sheet_endpoint = os.getenv('SHEET_ENDPOINT')
headers = {"Authorization": os.getenv('SHEET_TOKEN')}


for data in response.json()['exercises']:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": data['user_input'],
            "duration": data['duration_min'],
            "calories": data['nf_calories'],
        }

    }
    response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=headers)


