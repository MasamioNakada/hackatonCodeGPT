import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
backend_url = os.getenv('BACKEND_APP')
def validate_username(email:str):
    users = requests.get(backend_url+"/users/").json()
    for user in users:
        if email == user["email"]:
            return True
    raise "Usuario no encontrado"

def send_conversation(data:dict):
    res =requests.post(backend_url+"/users/conversations",json=data)
    print(res.json())

def get_all_conversation():
    res = requests.get(backend_url+"/users/conversations")
    return res.json()

def get_response_analizador(data:dict):
    url = "https://plus.codegpt.co/api/v1/agent/" + "3f98d3c8-8d50-460d-adfd-e9655a3e88a0"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + os.getenv("CODEGPT_API_KEY"),
    }
    data = {"messages": [{"role":"user","content":json.dumps(data)}]}
    response = requests.post(url, headers=headers, json=data)
    return response