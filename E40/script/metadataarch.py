import os

from docx import Document

from PyPDF2 import PdfReader


def metadata_docx(path):

    doc = Document(path)

    props = doc.core_properties

    return {

    "tipo": "DOCX",

    "autor": props.author,

    "título": props.title,

    "creado": props.created,

    "modificado": props.modified

    }


def metadata_pdf(path):

    pdf = PdfReader(path)

    info = pdf.metadata

    return {

    "tipo": "PDF",

    "autor": info.author,

    "título": info.title,

    "creado": info.creation_date,

    "modificado": info.modification_date

    }


# Carpeta a analizar

CARPETA = "E40"


print(f"📂 Analizando carpeta: {CARPETA}\n")

for archivo in os.listdir(CARPETA):
    ruta = os.path.join(CARPETA, archivo)
    if archivo.lower().endswith(".docx"):
        meta = metadata_docx(ruta)
    elif archivo.lower().endswith(".pdf"):
        meta = metadata_pdf(ruta)
    else:
        continue
    print(f"🗎 Archivo: {archivo}")
    for clave, valor in meta.items():
        print(f" {clave}: {valor}")
    print("-" * 40)