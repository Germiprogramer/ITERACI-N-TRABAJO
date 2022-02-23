# TRABAJO ITERACIÓN

La dirección de este repositorio GitHub es : https://github.com/carlospuigserver/ITERACI-N-TRABAJO.git


### EJERCICIO 07:  Edición de un número entero

* En este ejercicio tenemos que llevar a cabo un algoritmo que transforme un número entero n cualquiera en su representación en una base B ≥ 2 cualquiera. Cuando la base es superior a 36, se puede utilizar la representación de los números en base diez, pero separando cada cifra de la representación del número en base B mediante un separador convenido.





```
resultado=[]
print("Elige un número que quieras editar")

num=int(input())
print("Elige una base en la que quieras poner el número que has elegido")

base_num= int(input())


def edici(num,base_num):
  if base_num > 36:
    print(num)

  elif base_num < 2:
    print("La base no es válida")

  else:
    resultado.append(num%base_num)

    if num//base_num ==0:
      print(f"La solución es {resultado}")

    else:
      num=num//base_num
      edici(num, base_num)

  edici(num,base_num)
  ```



### EJERCICIO 08: Análisis de una cadena de caracteres

* Para realizar este ejercicio, debemos crear una cadena de caracteres con distintas partes separadas por un carácter separador específico. El objetivo es separar dichas partes y situarlas en una tabla de cadenas de caracteres. 






```
entrada = input("Introduce una cadena de texto separada por :" )

n = len(entrada)

SEPARADOR = ":"

lista = entrada.split(":")

print("""
nº      Cadena
""")

subcadenas = list(entrada).count(":")

for numero in range (subcadenas+1):
    posicion = numero +1
    print(posicion, "       ", lista[numero])


  
  
```









### EJERCICIO 09: Búsqueda de palabras en un diccionario

* Para llevar acabo este ejercicio, debemos crear un algoritmo el cual nos pida una palabra y a partir de ahí diferentes opciones, si queremos añadir otra palabra, si queremos eliminar una palabra en caso de haber añadido alguna, o borrar la primera, una opción de terminar el programa en cualquier momento, y una última opción de ordenar la palabra, para esta última opción, para cada palabra, crearemos una tabla y cada celda será ocupada por la palabra que le sigue en orden alfabético en el diccionario.



```
import sys

lista=[]

def adjuntar():
  print("Elige una palabra para introducirla en el diccionario")

  palabra= str(input())

  lista.append(palabra)
  print(lista)
  print("¿Deseas añadir palabras? elige entre 'si'o 'no' ")

  eleccion=str(input())

  if eleccion == "si"
    adjuntar()

  if eleccion == "no"

  elecc()


def eliminar():

  print ("Selecciona la palabra que desees borrar ")
  borrar=str(input())
  lista.remove(f"{borrar}")
  print(lista)
  elecc()


def ordenar():
  lista.sort()
  print(lista)


def elecc():
  print("Elige una de las siguientes opciones: adjuntar, eliminar, ordenar, o acabar")

  eleccion=str(input())

  if eleccion=="adjuntar"
    adjuntar()


  if eleccion=="eliminar"
    eliminar()

  if eleccion=="ordenar"
    ordenar()

  if eleccion=="acabar"
    print(lista)

    sys.exit

adjuntar()

```




### EJERCICIO 11:  Mcd de dos números enteros

* Para llevar acabo este ejercicio debemos crear un algoritmo que sea capaz de determinar el máximo común divisor de dos números enteros, dando una versión iterativa de dos opciones distintas, realizarlo mediante el método de Euclides, o mediante el método de sumas y restas.


```
elecc=int(input("De que manera quieres encontrar el mcd, a partir de Euclides o sumas y restas"))

num1=int(input("Escribe un número que quieras usar:"))

num2=int(input("Escribe otro número que quieras usar:")


if elecc == "Euclides":

  def mcd(num1,num2):
      if num2 == 0:
           return num1
      return mcd ( num2, num1 % num2)

  resultado= mcd ( num1, num2)
  print(f"El mcd resultante de {num1} y {num2} es {result}")


elif elecc == "sumas y restas":
  def mcd(num1, num2):
    if (num1 == 0):
        return num2

    if (num2 == 0):
        return num1

    if (num1 == num2):
        return num1

    if (num1 > num2):
        return mcd( num1-num2, num2)

    return mcd ( num1, num2-num1)  


  if(mcd(num1, num2)):
    result= mcd(num1, num2)
    print(f"El mcd  de {num1} y {num2} es {result})




else:
    print("En este caso no podemos realizar el mcd")

```



### EJERCICIO 12:

