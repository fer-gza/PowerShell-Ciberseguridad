from PIL import Image, ExifTags

def print_exif(path):
    img = Image.open(path)
    exif = img._getexif()
    
    if not exif:
        print("No hay EXIF")
        return

    readable = {}
    for tag, value in exif.items():
        tag_name = ExifTags.TAGS.get(tag, tag)
        readable[tag_name] = value

    for key, val in readable.items():
        print(f"{key}: {val}")

print_exif("pic1 1.jpg")
