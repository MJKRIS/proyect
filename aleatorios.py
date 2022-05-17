# importar aleatorios
import nacl.utils
import nacl.hash
import nacl.encoding

# rango de 12 variable
numeros = nacl.utils.random(12)
print("Numeros random:\n")

for char in numeros:
    print(str(char), end=" ")

print("\n\nNumeros en byte:\n")
print(numeros)

ascii = "".encode('ascii')
print("\n\nNumeros codificados con ascii:\n")
# Se genera la variable
numascii = nacl.hash.sha256(ascii, encoder=nacl.encoding.HexEncoder)
print(numascii)
