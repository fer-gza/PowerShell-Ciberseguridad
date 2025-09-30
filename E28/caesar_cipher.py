# caesar_cipher.py

VALID_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    " .,;:!?-()[]{}@#$/\\%&*+=<>\"'"
)

def encrypt(texto, clave):
    resultado = []
    n = len(VALID_CHARS)
    for ch in texto:
        if ch in VALID_CHARS:
            idx = VALID_CHARS.index(ch)
            resultado.append(VALID_CHARS[(idx + clave) % n])
        else:
            resultado.append(ch)
    return "".join(resultado)

def decrypt(texto, clave):
    resultado = []
    n = len(VALID_CHARS)
    for ch in texto:
        if ch in VALID_CHARS:
            idx = VALID_CHARS.index(ch)
            resultado.append(VALID_CHARS[(idx - clave) % n])
        else:
            resultado.append(ch)
    return "".join(resultado)

def load_dictionary(ruta):
    palabras = set()
    with open(ruta, encoding="utf-8") as f:
        for line in f:
            w = line.strip().lower()
            if w:
                palabras.add(w)
    return palabras

def brute_force_all(ciphertext, pct_letters=0.2):
    resultados = []
    for clave in range(len(VALID_CHARS)):
        pt = decrypt(ciphertext, clave)
        resultados.append((clave, pt))
    return resultados

def brute_force_dict(ciphertext, dict_words, pct_letters=0.2, pct_dict=0.5):
    candidatos = []
    for clave in range(len(VALID_CHARS)):
        pt = decrypt(ciphertext, clave)
        words = pt.split()
        if not words:
            continue
        only_letters = [w for w in words if w.isalpha()]
        if len(only_letters) / len(words) < pct_letters:
            continue
        count_in_dict = sum(1 for w in only_letters if w.lower() in dict_words)
        if count_in_dict / len(only_letters) >= pct_dict:
            candidatos.append((clave, pt))
    return candidatos
