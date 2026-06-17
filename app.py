from supabase import create_client
from dotenv import load_dotenv
import requests
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_TOKEN")


contatos = supabase.table("pessoas").select("*").execute().data

for contato in contatos:
    nome = contato["nome"]
    telefone = contato["telefone"]

    requests.post(
        f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text",
        json={
            "phone": telefone,
            "message": f"Olá, {nome} tudo bem com você?"
        }
    )

    print(f"Mensagem enviada para: {nome}")