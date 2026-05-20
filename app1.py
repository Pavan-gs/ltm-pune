import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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