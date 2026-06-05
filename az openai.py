import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://foundrypvn.cognitiveservices.azure.com/",
    api_key="E5dTYVgZuoZW7ttpD7TkSR0r3nvKNrdPwY9g31mvF6HoQupiDeOfJQQJ99CEACHYHv6XJ3w3AAAAACOGgoe8",
)

# pip install openai

from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="YOUR_OPENAI_KEY",
    api_version="2024-02-01",
    azure_endpoint="YOUR_OPENAI_ENDPOINT"
)

response = client.chat.completions.create(

    model="gpt-4o-mini",

    messages=[
        {
            "role": "user",
            "content": "What is the leave policy?"
        }
    ],

    extra_body={

        "data_sources": [

            {
                "type": "azure_search",

                "parameters": {

                    "endpoint": "YOUR_SEARCH_ENDPOINT",

                    "index_name": "YOUR_INDEX_NAME",

                    "authentication": {
                        "type": "api_key",
                        "key": "YOUR_SEARCH_KEY"
                    }
                }
            }
        ]
    }
)

print(response.choices[0].message.content)