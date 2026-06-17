from dotenv import load_dotenv
import os
import requests

load_dotenv()

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")

url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"

payload = {
    "phone": "5531975686344",
    "message": "Olá Paula, tudo bem?"
}

resposta = requests.post(url, json=payload)

print("Status:", resposta.status_code)
print("Resposta:", resposta.text)