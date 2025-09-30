# caesar_main.py

from caesar_cipher import encrypt, decrypt, load_dictionary, brute_force_all, brute_force_dict

DICT_PATH = "dictEsp.txt"

def main():
    dict_words = None

    while True:
        print("\n=== Menú César Avanzado ===")
        print("1) Cifrar")
        print("2) Descifrar")
        print("3) Descifrar todas")
        print("4) Crackear con diccionario")
        print("5) Salir")
        opcion = input("Elige opción (1-5): ").strip()

        if opcion == "1":
            texto = input("Texto a cifrar:\n")
            clave = int(input(f"Clave (0-{len(encrypt.__globals__['VALID_CHARS'])-1}): "))
            print("Resultado:", encrypt(texto, clave))

        elif opcion == "2":
            texto = input("Texto a descifrar:\n")
            clave = int(input(f"Clave (0-{len(decrypt.__globals__['VALID_CHARS'])-1}): "))
            print("Resultado:", decrypt(texto, clave))

        elif opcion == "3":
            texto = input("Texto cifrado:\n")
            for clave, pt in brute_force_all(texto):
                print(f"[{clave}] {pt}")

        elif opcion == "4":
            if dict_words is None:
                print("Cargando diccionario...", end="")
                dict_words = load_dictionary(DICT_PATH)
                print(" listo.")

            texto = input("Texto cifrado:\n")
            pct_letters = float(input("Umbral letras (0-1) [0.2]: ") or 0.2)
            pct_dict = float(input("Umbral diccionario (0-1) [0.5]: ") or 0.5)

            candidatos = brute_force_dict(texto, dict_words, pct_letters, pct_dict)
            if not candidatos:
                print("No se encontraron frases plausibles.")
            else:
                for clave, pt in candidatos:
                    print(f"[{clave}] {pt}")

        elif opcion == "5":
            print("Saliendo…")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
