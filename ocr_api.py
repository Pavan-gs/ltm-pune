from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI()

endpoint = "https://pvn-docintel.cognitiveservices.azure.com/"
api_key = "69v5yi7Z5EoAcY9aOKdCWfKipd1uNJf2ZyF6hYp0fXgWvCVcKJCtJQQJ99CEACYeBjFXJ3w3AAALACOGb7mF"

url = endpoint + "formrecognizer/documentModels/prebuilt-read:analyze?api-version=2023-07-31"


@app.post("/ocr")
async def perform_ocr(file: UploadFile = File(...)):

    file_bytes = await file.read()

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(
        url,
        headers=headers,
        data=file_bytes
    )

    operation_url = response.headers["operation-location"]

    result_response = requests.get(
        operation_url,
        headers={
            "Ocp-Apim-Subscription-Key": api_key
        }
    )

    return result_response.json()

# uvicorn ocr_api:app --reload
'''Enterprise Architecture
# React Frontend
↓
.NET Backend
↓
FastAPI OCR Wrapper
↓
Azure Document Intelligence
↓
OCR Result'''

'''“Unlike Azure ML, OCR services are already pretrained 
Microsoft-managed APIs. We directly consume the service endpoint instead 
of deploying our own model.”'''