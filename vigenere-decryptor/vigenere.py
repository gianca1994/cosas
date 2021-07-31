from functools import cache
from langdetect import detect_langs
import chardet
import os


alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

@cache
def decrypt_text(text, key):
    decrypted_message = ""
    i = 0
    for letter in text:
        suma = alphabet.find(letter) - alphabet.find(key[i % len(key)])
        module = int(suma) % len(alphabet)
        decrypted_message = decrypted_message + str(alphabet[module])
        i += 1
    return decrypted_message


def main():
    os.system("clear")

    text = str(input("Ingrese el texto a desencriptar: "))
    opt = int(input("Tiene la clave? 1- SI | 2- NO: "))

    if opt == 1:
        clave = str(input("Ingrese La clave para desencriptar: "))
        print("El mensaje encriptado es:")
        print(decrypt_text(text, clave))
    else:

        print("Comienzo de ataque por fuerza bruta al criptograma...")
        file = open('dictionary.txt', 'r')
        words = file.readlines()
        file.close()

        i = 0
        with open("result.txt", "w") as f:
            for word in words:
                
                i += 1
                decryptedText = decrypt_text(text, word.strip("\n"))
        
                if chardet.detect(decryptedText.encode())['encoding'] == 'ascii' and chardet.detect(decryptedText.encode())['confidence'] > 0.9999:
                    f.write(f"Key: {word} | Texto: {decryptedText}\n")
                    break

                print("Test numero: ", i)
        print("Finalizado!! Se genero un archivo llamado result.txt que contiene todos los posibles resultados....")
        input()
        
if __name__ == "__main__":
    main()
