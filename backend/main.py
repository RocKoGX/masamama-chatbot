from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from openai import OpenAI
from pathlib import Path
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "TU_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "ventas_masamama.csv"

df = pd.read_csv(CSV_PATH)

class Pregunta(BaseModel):
    pregunta: str

def generar_resumen():
    producto_top = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
    cliente_top = df.groupby("cliente")["total"].sum().sort_values(ascending=False)
    local_top = df.groupby("local")["total"].sum().sort_values(ascending=False)
    vendedor_top = df.groupby("vendedor")["total"].sum().sort_values(ascending=False)
    categoria_top = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

    return f"""
Productos más vendidos:
{producto_top}

Clientes que más compran:
{cliente_top}

Ventas por local:
{local_top}

Ventas por vendedor:
{vendedor_top}

Ventas por categoría:
{categoria_top}
"""

@app.get("/")
def inicio():
    return {"mensaje": "Backend de Masamama funcionando"}

@app.post("/chat")
def chat(data: Pregunta):
    resumen = generar_resumen()

    respuesta = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "system",
                "content": "Eres un analista de ventas para Masamama, una panadería y cafetería artesanal."
            },
            {
                "role": "user",
                "content": f"""
Resumen de ventas:
{resumen}

Pregunta:
{data.pregunta}

Responde de forma clara, breve y útil para el negocio.
"""
            }
        ]
    )

    return {
        "respuesta": respuesta.choices[0].message.content
    }