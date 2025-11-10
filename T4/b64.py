from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def derive_fernet_key(password: str) -> Fernet:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"fixed_salt_01",
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return Fernet(base64.urlsafe_b64encode(key))

# cipher_base64 = (
#    "" 
#)
#cipher_bytes = base64.b64decode(cipher_base64)

cipher_bytes = 'gAAAAABo-VBF3sGDnzkfXBcg8HCt1ICXMBQEUVnN1oVYhRvLhcM787DQcAh7g6VIdqVpX8yeFC21HRJVQXTE0RfNlGCjick95PfQq4y8XRnNHaIb5jPwU-GVkmi_YKJSt5bOIIrZNXymZZRoMbghHgyV5JcVmUYdpl4Hwifs3yOeaodZEIfOVBuxPyEerCizTR6hcGxXLaht'



claves = ["ciberseguridad", "informacion", "prenvencion"]

for clave in claves:
    try:
        fernet = derive_fernet_key(clave)
        mensaje = fernet.decrypt(cipher_bytes).decode()
        print(f"Clave correcta: {clave}")
        print("Mensaje descifrado:")
        print(mensaje)
        break
    except InvalidToken:
        print(f"Clave incorrecta: {clave}")