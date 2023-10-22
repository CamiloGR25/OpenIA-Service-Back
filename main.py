import os
import openai
from fastapi import FastAPI  # importar fastApi
from decouple import config # imnportar el funcionamiento de variable entorno

app = FastAPI()  # Inicia el servidor de la app

@app.get("/")
def root():  # Inicializa todo
    return {"service": "integracion Back OpenIA"}

@app.post("/chat")
def chat(pregunta: dict):

    openai.api_key = config("OPENAI_KEY")  # La llave de conexion con el modelo por medio de variable de entorno
   
    # Crear la configuracion del modelo:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": pregunta["pregunta"]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    print(response["choices"][0]["message"]["content"])
    return {"respuesta": response["choices"][0]["message"]["content"]} # retorna la respuesta de la pregunta
