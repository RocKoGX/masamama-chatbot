from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from openai import OpenAI, RateLimitError, AuthenticationError, APIConnectionError
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "http://127.0.0.1:5173"],
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

#Chatbot
from productos import productos
@app.post("/chat")
def chat(data: Pregunta):

    catalogo = "\n".join([
        f"""
ID: {p['id']}
Nombre: {p['nombre']}
Categoría: {p['categoria']}
Precio: {p['precio']}
Descripción: {p['descripcion']}
"""
        for p in productos
    ])

    try:

        respuesta = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
Eres un asistente virtual de Masamama.

Tu trabajo es recomendar productos
de panadería, cafetería y pastelería.

REGLAS:
- SOLO puedes recomendar productos del catálogo.
- NO inventes productos.
- Recomienda según precio y categoría.
- Si el usuario dice "barato", prioriza menor precio.
- Sé breve y amigable.
"""
                },
                {
                    "role": "user",
                    "content": f"""
Catálogo disponible:

{catalogo}

Usuario:
{data.pregunta}

Responde recomendando productos reales.
"""
                }
            ]
        )

        return {
            "respuesta":
            respuesta.choices[0].message.content
        }

    except RateLimitError:
        return {
            "respuesta":
            "El asistente está temporalmente sin crédito disponible. Intenta más tarde."
        }

    except AuthenticationError:
        return {
            "respuesta":
            "La API key de OpenAI es inválida o expiró."
        }

    except APIConnectionError:
        return {
            "respuesta":
            "No pude conectarme al servicio de IA. Revisa tu conexión."
        }

    except Exception as e:

        print("ERROR CHATBOT:", e)

        return {
            "respuesta":
            "Ocurrió un error inesperado en el chatbot."
        }