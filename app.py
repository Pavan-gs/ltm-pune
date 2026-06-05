# Simple ML + FastAPI + .NET + React Integration Guide

## Objective

In this exercise, participants will:

1. Build a very small ML model in Python
2. Expose the model using FastAPI
3. Run the FastAPI server locally
4. Call the API using Python requests library
5. Understand how .NET applications consume APIs
6. Understand how React applications communicate with backend APIs
7. Understand enterprise AI application architecture

---

# Final Architecture

```text
React Frontend
      ↓
.NET Backend API
      ↓
FastAPI ML Service
```

The important concept:

* Frontend handles user interaction
* Backend handles orchestration and security
* ML service handles predictions

---

# STEP 1 — Install Required Software

## Install Python

Download Python 3.11+

[https://www.python.org/downloads/](https://www.python.org/downloads/)

IMPORTANT:
While installing, enable:

```text
Add Python to PATH
```

---

## Install VS Code

Download:

[https://code.visualstudio.com/](https://code.visualstudio.com/)

Recommended Extensions:

* Python
* C#
* ES7 React Snippets

---

## Install .NET SDK

Download .NET 8 SDK:

[https://dotnet.microsoft.com/en-us/download](https://dotnet.microsoft.com/en-us/download)

Verify installation:

```bash
dotnet --version
```

---

## Install Node.js

Download LTS version:

[https://nodejs.org/](https://nodejs.org/)

Verify:

```bash
node -v
npm -v
```

---

# STEP 2 — Create Python Environment

Open VS Code terminal.

Create project folder:

```bash
mkdir ml-demo
cd ml-demo
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

## Windows

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
source venv/bin/activate
```

---

# STEP 3 — Install Python Libraries

Install required packages:

```bash
pip install pandas scikit-learn fastapi uvicorn requests
```

Explanation:

| Package      | Purpose               |
| ------------ | --------------------- |
| pandas       | Data handling         |
| scikit-learn | ML model creation     |
| fastapi      | Create backend API    |
| uvicorn      | Run FastAPI server    |
| requests     | Call APIs from Python |

---

# STEP 4 — Create ML Model + FastAPI

Create file:

```text
app.py
```

Paste the following code.

```python
# =========================================
# IMPORT REQUIRED LIBRARIES
# =========================================

# pandas is used for handling tabular data
import pandas as pd

# train_test_split helps split data into training and testing sets
from sklearn.model_selection import train_test_split

# LogisticRegression is a simple classification algorithm
from sklearn.linear_model import LogisticRegression

# accuracy_score helps evaluate model performance
from sklearn.metrics import accuracy_score

# FastAPI helps expose Python code as REST APIs
from fastapi import FastAPI

# uvicorn runs the FastAPI application server
import uvicorn


# =========================================
# CREATE SAMPLE DATASET
# =========================================

# We are creating a tiny dataset manually.
# Imagine this as customer data.

# age = customer age
# salary = customer salary
# purchased = whether customer purchased product

# 1 = Yes
# 0 = No

# In real projects, data usually comes from CSV/database.


data = {
    "age": [22, 25, 47, 52, 46, 56, 27, 30],
    "salary": [25000, 32000, 72000, 80000, 65000, 90000, 35000, 40000],
    "purchased": [0, 0, 1, 1, 1, 1, 0, 0]
}


# Convert dictionary into DataFrame
# DataFrame = table-like structure

df = pd.DataFrame(data)


# =========================================
# PREPARE FEATURES AND TARGET
# =========================================

# Features = input columns used for prediction
X = df[["age", "salary"]]

# Target = output column we want to predict
y = df["purchased"]


# =========================================
# SPLIT DATA
# =========================================

# We divide data into:
# - Training data
# - Testing data

# Training data helps model learn patterns
# Testing data checks model performance

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================================
# CREATE MODEL
# =========================================

# Logistic Regression is commonly used for:
# - Yes/No predictions
# - Classification problems

model = LogisticRegression()


# =========================================
# TRAIN MODEL
# =========================================

# fit() means:
# "Learn patterns from training data"

model.fit(X_train, y_train)


# =========================================
# EVALUATE MODEL
# =========================================

# Predict on test data
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy}")


# =========================================
# CREATE FASTAPI APPLICATION
# =========================================

# FastAPI helps expose Python functions as APIs.
# APIs allow applications to communicate.

app = FastAPI()


# =========================================
# CREATE PREDICTION ENDPOINT
# =========================================

# POST endpoint:
# http://127.0.0.1:8000/predict

@app.post("/predict")
def predict(data: dict):

    # Read input values from request body
    age = data["age"]
    salary = data["salary"]

    # Convert input into DataFrame
    # because model expects tabular format
    input_data = pd.DataFrame({
        "age": [age],
        "salary": [salary]
    })

    # Generate prediction
    result = model.predict(input_data)

    # Convert numeric prediction into readable text
    if result[0] == 1:
        prediction = "Likely to Purchase"
    else:
        prediction = "Not Likely to Purchase"

    # Return JSON response
    return {
        "prediction": prediction
    }


# =========================================
# RUN APPLICATION
# =========================================

# This starts backend server locally.

# localhost means:
# running on your own machine

# port 8000 means:
# application accessible on port 8000

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

---

# STEP 5 — Run FastAPI Server

Open terminal:

```bash
python app.py
```

Expected Output:

