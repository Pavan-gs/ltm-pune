import requests

url = "http://127.0.0.1:8000/predict"

payload = {
    "age": 45,
    "salary": 75000
}

response = requests.post(url, json=payload)

print(response.json())

'''
client.py
↓
HTTP POST Request
↓
FastAPI receives request
↓
Model predicts result
↓
FastAPI returns JSON
↓
client.py prints result

“This Python script is behaving exactly like a frontend application or backend application. 
It’s sending a request to the FastAPI backend and printing the response. 
In a real-world scenario, this could be part of a larger application where users input their data through a web interface, 
and this script sends that data to the backend for prediction and displays the result to the user.”'''