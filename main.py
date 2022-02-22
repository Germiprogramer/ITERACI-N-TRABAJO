entrada = input("Introduce una cadena de texto separada por :")

n = len(entrada)

print(entrada[2])

SEPARADOR = ":"

for posicioncaracter in range(n):
  if entrada[posicioncaracter] == ":":
    