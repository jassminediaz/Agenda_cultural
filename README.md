# Agenda_cultural

Proyecto: Website académico / Tech sobre agenda cultural

## Objetivo
Demostrar un flujo reproducible de extracción, procesamiento y publicación de datos culturales utilizando Python y GitHub Pages, con fines académicos y de comunicación digital.

## Fuente
Agenda cultural obtenida desde una web pública de eventos culturales  
(consulta automatizada mediante requests + BeautifulSoup).

## Outputs

**Datasets generados:**

- `data/raw.csv`  
  Datos extraídos directamente del sitio web (eventos culturales, títulos y enlaces).

- `data/clean.csv`  
  Versión limpia del dataset: sin valores nulos, texto normalizado y columnas ordenadas.

- `data/summary.csv`  
  Resumen analítico con frecuencia de palabras y términos culturales dominantes.

## Flujo de trabajo

1. Web scraping de eventos culturales
2. Limpieza y normalización de texto
3. Generación de métricas descriptivas
4. Publicación de datos y visualización en una web estática

## Cómo correr el proyecto

Instalar dependencias:
```bash
pip install requests beautifulsoup4 pandas

Website: publicado con GitHub Pages en /docs.
