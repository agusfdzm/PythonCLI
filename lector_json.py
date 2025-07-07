import json
import os

RUTA_ARCHIVO = "data.json"

def leer():
    if not os.path.isfile(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def escribir(data):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
