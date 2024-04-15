
import requests

patient = {
    "gender": "Female",	
    "age": 36,	
    "hypertension": 0,	
    "heart_disease": 0,	
    "ever_married": "No",	
    "work_type": "Private",	
    "Residence_type": "Urban",	
    "avg_glucose_level": 180.5,	
    "bmi": 36.6,	
    "smoking_status": "Never smoked"
}

# Location of my server
url = "http://127.0.0.1:8989/predict"

# Send request
resp = requests.post(url, json=patient)

# Print result
print(resp.json())