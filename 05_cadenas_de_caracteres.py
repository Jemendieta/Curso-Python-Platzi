#  CADENAS DE CARACTERES EN PYTHON

# Métodos: 

# nombre = input("¿Cuál es tu nombre?: ")
# # al ingresar nuestro nombre es probable que hayamos colocado la priemra letra en minúsculas, esto podemos corregirlo, hacemos lo siguiente
# nombre.upper() # upper es un método (función para un tipo de dato en especial), con esto cambiamos el nombre a mayúscula
# nombre.capitalize() # con este método convertimos la primera letra del nombre en mayúscula
# nombre = nombre.capitalize() # con esto guardamos dentro de la variable nombre a capitalize()
# nombre = nombre.strip()# con esto eliminamos los espacios que no necesitamos en la cadena de caracteres
# nombre = nombre.lower() # con este método, convertimos el nombre a minúsculas
# nombre = nombre.replace("o","a") # el método replace requiere de dos parámetros, el primero es la letra que buscaremos, y el segundo el que colocaremos en lugar del primero

# letra = nombre[1] # con esto mostramos el caracter que se encuentra en la posición que indiquemos entre los corchetes, cero equivale al primer caracter, 1 al segundo y así sucesvamente
# print(nombre)
# print(letra)
# print(len(nombre)) # con len mostramos la cantidad de caractereres de mi cadena de texto

# SLICES o Revanadas: lo que nos permite esto es separar en partes mas pequeñas las cadenas de texto

nombre = "Enrique"
print(nombre[0:3]) # con esto le decimos a la varible que tomaremos desde el primer índice hasta antes del tercero, es decir nos mostraría Enr
print(nombre[:3]) # esta es otra forma de hacer lo mismo, pero obviando el primer índice
print(nombre[3:]) # de la misma forma podemos obviar el último índice, aquí nos mostraría a partir del 4 caracter en adelante
print(nombre[1:6])
print(nombre[1:6:2]) # desde el caracter 1 hasta el 6 pero de dos en dos, devuelve niu
print(nombre[::]) # nos devuelve el nombre completo
print(nombre[1::2]) # desde el índice 1 hasta el final en pasos de dos en dos
print(nombre[::-1]) # desde el principio hasta el final pero en pasos negativos(desde el final hasta el principio de uno en uno) mostrando el nombre al revez