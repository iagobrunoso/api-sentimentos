
"""
GRUPO:

IAGO BRUNO
PATRÍCIA SAN IZIDRO
FÁBIO RIOS

"""

from fastapi import FastAPI
from pydantic import BaseModel

# Modelo de dados que a API vai receber
class Texto(BaseModel):
    mensagem: str

app = FastAPI()

# Método GET
@app.get("/")
def home():
    return {"mensagem": "API de análise de sentimentos funcionando"}

# Método POST
@app.post("/analisar")
def analisar(texto: Texto):

    frase = texto.mensagem

    # Simulador para analisar sentimento
    if "bom" in frase.lower():
        sentimento = "positivo"

    elif "ruim" in frase.lower():
        sentimento = "negativo"

    else:
        sentimento = "neutro"

    return {
        "texto": frase,
        "sentimento": sentimento
    }



