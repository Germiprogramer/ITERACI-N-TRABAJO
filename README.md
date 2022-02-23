# TRABAJO ITERACIÓN

La dirección de este repositorio GitHub es : https://github.com/carlospuigserver/ITERACI-N-TRABAJO.git


### EJERCICIO 07:

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

