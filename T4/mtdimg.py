from PIL import Image
import piexif
import pprint
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
import os


def extract_exif(image_path):
    img = Image.open(image_path)
    if "exif" in img.info:
        exif_data = piexif.load(img.info["exif"])
        print(f"[EXIF] {image_path}")
        pprint.pprint(exif_data)
        
        if piexif.ImageIFD.ImageDescription in exif_data["0th"]:
            desc = exif_data["0th"][piexif.ImageIFD.ImageDescription]
            print("ImageDescription:", desc.decode() if isinstance(desc, bytes) else desc)
    else:
        print(f"No EXIF en {image_path}")


def extract_png_text(image_path):
    img = Image.open(image_path)
    print(f"[tEXt] {image_path}")
    for k, v in img.text.items():
        try:
            print(f"{k}: {v}")
        except UnicodeEncodeError:
            print(f"{k}: {v.encode('utf-8', errors='replace').decode('utf-8')}")


def decode_base64_field(text):
    try:
        decoded = base64.b64decode(text).decode()
        print("Base64 decodificado:", decoded)
        return decoded
    except Exception as e:
        print("No es base64 válido:", e)
        return None


def derive_fernet(passphrase, salt=b"sal_fija_del_equipo"):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(passphrase.encode()))
    return Fernet(key)


def decrypt_message(ciphertext, fernet):
    try:
        decrypted = fernet.decrypt(ciphertext)
        print("Mensaje descifrado:", decrypted.decode())
        return decrypted.decode()
    except Exception as e:
        print("Error al descifrar:", e)
        return None



def analizar_imagenes_en_directorio(directorio="."):
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(('.png', '.jpeg', '.jpg')):
            ruta = os.path.join(directorio, archivo)
            print(f"\nAnalizando: {archivo}")
            extract_exif(ruta)
            if archivo.lower().endswith('.png'):
                extract_png_text(ruta)


if __name__ == "__main__":
    analizar_imagenes_en_directorio()