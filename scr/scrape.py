import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://heptagrama.com/agenda-cultural-lima.htm"

def limpiar_texto(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

def main():
    resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    eventos = []

    # Cada evento listado está como <li> o <p> con texto repetido
    # En este caso el contenido es un cuerpo de texto con saltos
    cuerpo = soup.get_text(separator="\n").split("\n")

    # filtramos líneas útiles
    for linea in cuerpo:
        linea = limpiar_texto(linea)
        # solo guardamos líneas con texto y con alguna fecha o palabra clave
        if len(linea) > 20 and any(month in linea.lower() for month in [
            "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "set", "oct", "nov", "dic"
        ]):
            eventos.append({"evento": linea})

    df = pd.DataFrame(eventos).drop_duplicates()

    df.to_csv("data/raw.csv", index=False, encoding="utf-8")

    print(f"✅ {len(df)} eventos guardados en data/raw.csv")

if __name__ == "__main__":
    main()
