import requests

# -----------------------------------------
# AZURE DOCUMENT INTELLIGENCE DETAILS
# -----------------------------------------

# Replace with your endpoint
endpoint = "https://pvn-docintel.cognitiveservices.azure.com/"

# Replace with your API key
api_key = "69v5yi7Z5EoAcY9aOKdCWfKipd1uNJf2ZyF6hYp0fXgWvCVcKJCtJQQJ99CEACYeBjFXJ3w3AAALACOGb7mF"

# OCR API URL
url = endpoint + "formrecognizer/documentModels/prebuilt-read:analyze?api-version=2023-07-31"

# -----------------------------------------
# HEADERS
# -----------------------------------------

headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/octet-stream"
}

# -----------------------------------------
# READ FILE
# -----------------------------------------

# Replace with your image/pdf path
file_path = "invoice.pdf"

with open(file_path, "rb") as f:
    
    # Send POST request to OCR API
    # Note: Azure OCR expects binary data, so we read the file in binary mode and send it as the request body.
    response = requests.post(
        url,
        headers=headers,
        data=f
    )

# -----------------------------------------
# CHECK RESPONSE
# -----------------------------------------

print("Status Code:", response.status_code)

# Azure OCR initially returns operation-location header
operation_url = response.headers["operation-location"]

print("Operation URL:")
print(operation_url)

# -----------------------------------------
# GET FINAL OCR RESULT
# -----------------------------------------

result_response = requests.get(
    operation_url,
    headers={
        "Ocp-Apim-Subscription-Key": api_key
    }
)

# Print OCR result
print(result_response.json())

'''Python Script
↓
Azure Document Intelligence API
↓
OCR Processing
↓
JSON Response Returned'''
