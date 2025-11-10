from PIL import Image

def extract_lsb_message(image_path):
    img = Image.open(image_path).convert("RGBA")
    pixels = list(img.getdata())

    bits = []
    for pixel in pixels:
        for channel in pixel:  
            bits.append(channel & 1)  

    
    bytes_out = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit
        bytes_out.append(byte)
        if bytes_out[-2:] == b"\x00\x00":
            break

    
    mensaje = bytes_out[:-2].decode(errors="replace")
    return mensaje

mensaje_oculto = extract_lsb_message("pic2 1.png") 
print("Palabra clave oculta (pic2 1.png):", repr(mensaje_oculto))

mensaje_oculto = extract_lsb_message("pic5 1.png") 
print("Palabra clave oculta (pic5 1.png):", repr(mensaje_oculto))

mensaje_oculto = extract_lsb_message("pic6 1.png") 
print("Palabra clave oculta (pic6 1.png):", repr(mensaje_oculto))

