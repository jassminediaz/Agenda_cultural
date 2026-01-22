import re
import pandas as pd

STOPWORDS_ES = {
    "de","la","el","y","en","a","un","una","para","por","con",
    "del","los","las","al","se","su","sus","una","uno"
}

STOPWORDS_EN = {
    "the","and","to","of","in","for","on","with","a","an"
}

def limpiar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

def tokenizar(texto: str):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s-]", " ", texto)
    tokens = [t for t in texto.split() if len(t) >= 3]
    tokens = [
        t for t in tokens
        if t not in STOPWORDS_ES and t not in STOPWORDS_EN
    ]
    return tokens

def main():
    # =====================
    # 1. Leer datos crudos
    # =====================
    df = pd.read_csv("data/raw.csv")

    # suponemos que la columna se llama "evento"
    df["evento"] = df["evento"].fillna("").astype(str)

    # =====================
    # 2. CLEAN.CSV
    # =====================
    df_clean = df.copy()
    df_clean["evento"] = df_clean["evento"].apply(limpiar_texto)

    # eliminar filas vacías
    df_clean = df_clean[df_clean["evento"] != ""]

    df_clean.to_csv(
        "data/clean.csv",
        index=False,
        encoding="utf-8"
    )

    # =====================
    # 3. SUMMARY.CSV
    # =====================
    tokens_totales = []

    for evento in df_clean["evento"]:
        tokens_totales.extend(tokenizar(evento))

    resumen = (
        pd.Series(tokens_totales)
        .value_counts()
        .head(20)
        .reset_index()
        .rename(columns={"index": "palabra", 0: "frecuencia"})
    )

    resumen.to_csv(
        "data/summary.csv",
        index=False,
        encoding="utf-8"
    )

    print("✅ clean.csv creado")
    print("✅ summary.csv creado")

if __name__ == "__main__":
    main()
