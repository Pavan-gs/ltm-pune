import requests

url = "http://127.0.0.1:8000/predict"

payload = {
    "age": 45,
    "salary": 75000
}

response = requests.post(url, json=payload)

print(response.json())