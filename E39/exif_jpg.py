#!/usr/bin/env python3
# exif_mostrar_todo.py
# Requiere: pip install pillow piexif

from PIL import Image
import piexif
import pprint

def rational_to_float(r):
    """Convierte un rational (num, den) a float; acepta tuples o int/float."""
    try:
        return r[0] / r[1]
    except Exception:
        return float(r)

def dms_to_decimal(dms):
    """Convierte DMS en formato EXIF (tupla de rationals) a decimal."""
    deg = rational_to_float(dms[0])
    minu = rational_to_float(dms[1])
    sec = rational_to_float(dms[2])
    return deg + (minu / 60.0) + (sec / 3600.0)

def decode_if_byte(value):
    """Intenta decodificar bytes a str, si aplica."""
    if isinstance(value, (bytes, bytearray)):
        try:
            return value.decode('utf-8', errors='replace')
        except Exception:
            return repr(value)
    return value

def show_all_exif(path):
    """Muestra en consola todos los tags EXIF y, si hay GPS, imprime coordenadas decimales."""
    img = Image.open(path)
    exif_bytes = img.info.get("exif")
    if not exif_bytes:
        print("No se encontró EXIF en la imagen.")
        return

    exif_dict = piexif.load(exif_bytes)

    print("=== EXIF completo por IFD ===")
    for ifd_name in exif_dict:
        if ifd_name == "thumbnail":
            continue
        print(f"\n--- IFD: {ifd_name} ---")
        entries = exif_dict[ifd_name]
        if not entries:
            print(" (vacío)")
            continue
        for tag, val in entries.items():
            # Obtener nombre humano del tag si existe
            try:
                tag_name = piexif.TAGS[ifd_name][tag]["name"]
            except KeyError:
                tag_name = str(tag)
            display_val = val
            # Decodificar bytes cuando corresponda
            if isinstance(val, (bytes, bytearray)):
                display_val = decode_if_byte(val)
            # Para listas/tuplas de rationals no convertir aquí (se muestra crudo)
            print(f"{tag_name} ({tag}): {display_val}")

    # Manejo específico de GPS para convertir a decimal y mostrar más legible
    gps = exif_dict.get("GPS", {})
    if gps:
        print("\n=== GPS (interpretado) ===")
        lat = gps.get(piexif.GPSIFD.GPSLatitude)
        lat_ref = gps.get(piexif.GPSIFD.GPSLatitudeRef)
        lon = gps.get(piexif.GPSIFD.GPSLongitude)
        lon_ref = gps.get(piexif.GPSIFD.GPSLongitudeRef)
        if lat and lon and lat_ref and lon_ref:
            try:
                lat_dec = dms_to_decimal(lat)
                lon_dec = dms_to_decimal(lon)
                lat_ref_str = decode_if_byte(lat_ref)
                lon_ref_str = decode_if_byte(lon_ref)
                if lat_ref_str in ("S", "s"):
                    lat_dec = -lat_dec
                if lon_ref_str in ("W", "w"):
                    lon_dec = -lon_dec
                print(f"Latitud (decimal):  {lat_dec}")
                print(f"Longitud (decimal): {lon_dec}")
                print(f"Lat ref: {lat_ref_str}  Lon ref: {lon_ref_str}")
            except Exception as e:
                print("No se pudo convertir GPS a decimal:", e)
        else:
            print("GPS IFD presente pero incompleto. Campos encontrados:")
            for tag, val in gps.items():
                try:
                    tag_name = piexif.TAGS["GPS"][tag]["name"]
                except KeyError:
                    tag_name = str(tag)
                print(f"{tag_name} ({tag}): {val}")
    else:
        print("\nNo se encontró IFD GPS.")

if __name__ == "__main__":
    INPUT_PATH = "pic6 1.png" 
    print(f"Leyendo metadatos EXIF de: {INPUT_PATH}\n")
    try:
        show_all_exif(INPUT_PATH)
    except FileNotFoundError:
        print("Archivo no encontrado. Verifica el nombre y la ruta.")
    except Exception as e:
        print("Error al leer EXIF:", e)