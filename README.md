# 📰 Scraper de Noticias de la UJI (Universitat Jaume I)

Este proyecto implementa un **scraper automatizado en Python** para recopilar noticias publicadas en la web institucional de la **Universitat Jaume I (UJI)**.  
El script navega por el buscador de noticias, accede a cada entrada individual y descarga su contenido en **tres formatos**: HTML, texto plano y Markdown, generando además un **índice JSON estructurado**.

El proceso soporta **múltiples idiomas**:
- Valenciano (`va`)
- Castellano (`es`)
- Inglés (`en`)


## 🎯 Objetivo del script

- Descargar noticias históricas de la UJI de forma automatizada.
- Normalizar el contenido en distintos formatos (HTML / TXT / MD).
- Facilitar su posterior análisis, indexación o uso en datasets.
- Generar un índice JSON con metadatos de todas las noticias procesadas.


## 🚀 Funcionalidades principales

- Navegación por páginas del buscador de noticias de la UJI.
- Extracción de enlaces individuales a noticias.
- Acceso a versiones multilingües de cada noticia.
- Parsing de contenido mediante **BeautifulSoup**.
- Conversión de HTML a Markdown mediante **markdownify**.
- Guardado automático de archivos.
- Generación incremental de un índice JSON (`index.json`).


## 🧠 Flujo general de ejecución

1. Se itera sobre páginas del buscador de noticias.
2. En cada página se recopilan enlaces a noticias.
3. Para cada noticia:
   - Se obtiene la versión original.
   - Se consulta la versión en castellano.
   - Se consulta la versión en inglés.
4. Se extraen:
   - Título
   - Subtítulo (si existe)
   - Fecha de publicación
   - Contenido textual
5. Se guarda la noticia en:
   - HTML original
   - Texto plano
   - Markdown
6. Se añade una entrada al índice JSON.
7. El índice se guarda tras procesar cada conjunto.


## 📂 Estructura de carpetas generada

```
UJI/
├── html/
│   └── 2025/
│       ├── va/
│       ├── es/
│       └── en/
├── plain/
│   └── 2025/
│       ├── va/
│       ├── es/
│       └── en/
├── md/
│   └── 2025/
│       ├── va/
│       ├── es/
│       └── en/
└── index.json
```

Cada noticia se nombra como:

```
noticia<INDEX>.html
noticia<INDEX>.txt
noticia<INDEX>.md
```


## 🧰 Requisitos

### 📦 Dependencias de Python

- `requests`
- `beautifulsoup4`
- `markdownify`
- `json` (librería estándar)
- `os` (librería estándar)

Instalación:

```bash
pip install requests beautifulsoup4 markdownify
```


## ▶️ Ejecución

Simplemente ejecuta el script:

```bash
python scraper_uji.py
```

⚠️ Asegúrate previamente de que las carpetas de destino existen o añade creación automática de directorios (`os.makedirs`).


## 📄 Ejemplo de entrada en el índice JSON

```json
{
  "source": "https://www.uji.es/com/noticies/...",
  "title": "La UJI impulsa un nuevo proyecto",
  "subtitle": "Innovación y transferencia",
  "date": "12/07/2025",
  "path2html": "./html/2025-07/va/noticia7046.html",
  "path2txt": "./plain/2025-07/va/noticia7046.txt",
  "path2md": "./md/2025-07/va/noticia7046.md"
}
```

## 💰 Financiación

Este recurso está financiado por el Ministerio para la Transformación Digital y de la Función Pública — Financiado por la UE – NextGenerationEU, en el marco del proyecto Desarrollo de Modelos ALIA.

## 🙏 Agradecimientos

Expresamos nuestro agradecimiento a todas las personas e instituciones que han contribuido al desarrollo de este recurso.

Agradecimientos especiales a:

[Proveedores de datos]

[Proveedores de soporte tecnológico]

Asimismo, reconocemos las contribuciones financieras, científicas y técnicas del Ministerio para la Transformación Digital y de la Función Pública – Financiado por la UE – NextGenerationEU dentro del marco del proyecto Desarrollo de Modelos ALIA.

## 📚 Referencia

Por favor, cita este conjunto de datos usando la siguiente entrada BibTeX:

```
@misc{scraper_alia_uji_2025,
  author       = {Espinosa Zaragoza, Sergio and Sep{\'u}lveda Torres, Robiert and Mu{\~n}oz Guillena, Rafael and Consuegra-Ayala, Juan Pablo},
  title        = {ALIA_UJI Scraper}, 
  year         = {2025},
  institution  = {Language and Information Systems Group (GPLSI) and Centro de Inteligencia Digital (CENID), University of Alicante (UA)},
  howpublished = {\url{https://github.com/gplsi/scraper-alia-uji}}
}
```

## ⚠️ Aviso Legal

Este recurso puede contener sesgos o artefactos no intencionados.
Cualquier tercero que utilice o implemente sistemas basados en este recurso es el único responsable de garantizar un uso conforme, seguro y ético, incluyendo el cumplimiento de las normativas relevantes en materia de IA y protección de datos.

La Universidad de Alicante, como creadora y propietaria del recurso, no asume ninguna responsabilidad por los resultados derivados del uso por parte de terceros.

## 📜 Licencia

Licencia Apache, Versión 2.0
