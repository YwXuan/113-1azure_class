import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()



client = AzureOpenAI(
  azure_endpoint = os.getenv("w11_azure_endpoint"),
  api_key= os.getenv("w11_api_key"),
  api_version = os.getenv("w11_api_version")

)

response = client.chat.completions.create(
    model="gpt-4", # model = "deployment_name".
    messages=[
        {"role": "user", "content":  "Plan a trip to china a week"},
    ]
)

print(response.choices[0].message.content)