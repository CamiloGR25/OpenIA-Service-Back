from fastapi import FastAPI #importar fastApi

app= FastAPI() #Inicia el servidor de la app

@app.get("/")

def root():  #Inicializa todo
    return{
        "service":"integracion Back OpenIA"
    }