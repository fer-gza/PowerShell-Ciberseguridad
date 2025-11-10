from PIL import Image
import json

def extract_png_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            info_serializable = {k: str(v) for k, v in img.info.items()}

            metadata = {
                "format": img.format,
                "mode": img.mode,
                "size": img.size,
                "info": info_serializable
            }

            return metadata
    except IOError:
        return "No se pudo abrir la imagen."


file_path = "pic1 1.jpg"
metadata = extract_png_metadata(file_path)
print(f"Metadatos de {file_path}:")
print(json.dumps(metadata, indent=4))
