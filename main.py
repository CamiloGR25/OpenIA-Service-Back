import os
import openai
from fastapi import FastAPI #importar fastApi

app= FastAPI() #Inicia el servidor de la app

@app.get("/")

def root():  #Inicializa todo
    return{
        "service":"integracion Back OpenIA"
    }

@app.post("/chat")
def chat():
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": ""
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return{
        "service":"Ingresando"
    }