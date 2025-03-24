import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Gender": 1,  
    "Age": 25,  
    "Height": 175,  
    "Weight": 70,  
    "Duration": 30,  
    "Heart_Rate": 110,  
    "Body_Temp": 36.5  
}

response = requests.post(url, json=data)
print("Response:", response.json())
