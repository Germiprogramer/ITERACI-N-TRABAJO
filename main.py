#EJERCICIO 8

entrada = input("Introduce una cadena de texto separada por :" )

n = len(entrada)

SEPARADOR = ":"

for posicioncaracter in range(n):
  if entrada[posicioncaracter] == ":":
    print(entrada[0:(posicioncaracter-1)])
    print(entrada[(posicioncaracter+1):n])

lista = list(entrada)
print(lista)