from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import json
import os
import urllib.error
import urllib.request

from productos import productos

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = FastAPI()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_PATH = BASE_DIR / "ventas_masamama.csv"

df = pd.read_csv(CSV_PATH)


class Pregunta(BaseModel):
    pregunta: str


def llamar_gemini(system_prompt: str, user_prompt: str) -> str:
    if not GOOGLE_API_KEY:
        raise ValueError("Falta configurar GOOGLE_API_KEY en el archivo .env")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent"
    )
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_prompt}],
            }
        ],
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": GOOGLE_API_KEY,
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    candidates = data.get("candidates", [])
    if not candidates:
        return "No pude generar una respuesta en este momento."

    parts = candidates[0].get("content", {}).get("parts", [])
    return "".join(part.get("text", "") for part in parts).strip()


def generar_resumen():
    producto_top = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
    cliente_top = df.groupby("cliente")["total"].sum().sort_values(ascending=False)
    local_top = df.groupby("local")["total"].sum().sort_values(ascending=False)
    vendedor_top = df.groupby("vendedor")["total"].sum().sort_values(ascending=False)
    categoria_top = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

    return f"""
Productos mas vendidos:
{producto_top}

Clientes que mas compran:
{cliente_top}

Ventas por local:
{local_top}

Ventas por vendedor:
{vendedor_top}

Ventas por categoria:
{categoria_top}
"""


@app.get("/")
def inicio():
    return {"mensaje": "Backend de Masamama funcionando"}


@app.post("/chat")
def chat(data: Pregunta):
    catalogo = "\n".join(
        [
            f"""
ID: {p['id']}
Nombre: {p['nombre']}
Categoria: {p['categoria']}
Precio: {p['precio']}
Descripcion: {p['descripcion']}
"""
            for p in productos
        ]
    )

    system_prompt = """
Eres un asistente virtual de Masamama.

Tu trabajo es recomendar productos de panaderia, cafeteria y pasteleria.

REGLAS:
- SOLO puedes recomendar productos del catalogo.
- NO inventes productos.
- Recomienda segun precio y categoria.
- Si el usuario dice "barato", prioriza menor precio.
- Se breve y amigable.
- No uses emojis.
- No uses Markdown, negritas, asteriscos ni bloques de texto largos.
- Escribe en formato claro y profesional, separado por lineas.
- Usa esta estructura:
  Saludo breve.
  Recomendaciones:
  1. Producto - precio - motivo breve.
  2. Producto - precio - motivo breve.
  Pregunta final corta.
"""
    user_prompt = f"""
Catalogo disponible:

{catalogo}

Usuario:
{data.pregunta}

Responde recomendando productos reales.
No uses Markdown ni emojis. Separa la respuesta con saltos de linea.
"""

    try:
        respuesta = llamar_gemini(system_prompt, user_prompt)
        return {"respuesta": respuesta}

    except urllib.error.HTTPError as e:
        error = e.read().decode("utf-8", errors="ignore")
        print("ERROR GEMINI:", error)

        if e.code in (401, 403):
            return {
                "respuesta": "La API key de Google/Gemini es invalida o no tiene permisos."
            }

        if e.code == 429:
            return {
                "respuesta": "El asistente esta temporalmente sin cuota disponible. Intenta mas tarde."
            }

        return {
            "respuesta": (
                "El servicio de IA no pudo responder. "
                f"Codigo {e.code}. Revisa la terminal del backend para mas detalle."
            )
        }

    except urllib.error.URLError:
        return {"respuesta": "No pude conectarme al servicio de IA. Revisa tu conexion."}

    except ValueError as e:
        return {"respuesta": str(e)}

    except Exception as e:
        print("ERROR CHATBOT:", e)
        return {"respuesta": "Ocurrio un error inesperado en el chatbot."}
