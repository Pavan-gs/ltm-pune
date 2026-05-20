import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

# -----------------------------------------
# SAMPLE DATASET
# -----------------------------------------

data = {
    "age": [22, 25, 47, 52, 46, 56, 27, 30],
    "salary": [25000, 32000, 72000, 80000, 65000, 90000, 35000, 40000],
    "purchased": [0, 0, 1, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

# -----------------------------------------
# FEATURES AND TARGET
# -----------------------------------------

X = df[["age", "salary"]]
y = df["purchased"]

# -----------------------------------------
# TRAIN TEST SPLIT
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------------
# MODEL TRAINING
# -----------------------------------------

model = LogisticRegression()

model.fit(X_train, y_train)

# -----------------------------------------
# MODEL EVALUATION
# -----------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy}")

# -----------------------------------------
# FASTAPI APP
# -----------------------------------------

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# “CORS allows frontend applications running on different ports/domains to communicate with backend APIs.”

'''FastAPI app becomes:

Reusable ML Prediction Service

“The ML service does not care whether requests come from Python, .NET, React, mobile apps, or other systems.”

'''
# -----------------------------------------
# PREDICTION API
# -----------------------------------------

@app.post("/predict")
def predict(data: dict):

    age = data["age"]
    salary = data["salary"]

    input_data = pd.DataFrame({
        "age": [age],
        "salary": [salary]
    })

    result = model.predict(input_data)

    if result[0] == 1:
        prediction = "Likely to Purchase"
    else:
        prediction = "Not Likely to Purchase"

    return {
        "prediction": prediction
    }

# -----------------------------------------
# RUN SERVER
# -----------------------------------------

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

 '''Browser Swagger UI
↓
HTTP Request
↓
FastAPI Endpoint
↓
Prediction
↓
JSON Response
“FastAPI follows OpenAPI standards to automatically generate API documentation.”
“Backend APIs are usually tested independently before frontend integration.”'''

'''FastAPI (app.py)

Responsible for:

ML prediction
exposing API

 .NET Backend (Program.cs)

Responsible for:

orchestration
security
validation
calling ML service

React (App.js)

Responsible for:

user interaction
displaying predictions

“Modern AI systems are usually composed of multiple small services communicating through APIs.”

React Frontend (localhost:3000)
            ↓
.NET Backend API
            ↓
FastAPI ML Service (localhost:8000)
            ↓
ML Model'''

'''“We retain FastAPI because our ML model is built in Python. 
FastAPI exposes the model as a reusable API service that can be consumed by 
enterprise applications like .NET backends and React frontends.”'''

'''“FastAPI is one of the most commonly used frameworks for exposing Python AI/ML models as APIs. 
It’s popular because it’s lightweight, fast, and integrates very well with modern AI workflows.”'''