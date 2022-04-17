#* 1 Mi Carrrera en Python

# print('Hola Jorge desde Python')
# print(25**(1/2))

#* 2 Trabajando con operaciones mateméticas

# print(5 + 5) 
# print(5 - 5)
# print(5 * 5) 
# print(15 / 3) 
# print(15 % 5) 
# print(15 // 4) 
# print(2**3)#potencia de 2 
# print( 25 ** (1/2)) #Raíz cuadrada


#* 3 Trabajando con Variables en Python

# Una variable es una caja o lugar en donde puedo guardar objetos: numeros, textos, etc.
# El identificador de mi variable no puede comenzar con un número y debe estar en minúsculas.
# Las palabras dentro del mismo se separan con un guión bajo.

# numero1 = 3
# numero2 = 4
# print(numero1 + numero2)
# print(numero1 * numero2)

#* 4 Tipos de datos primitivs en Python

# números enteros
# edad = 35 

# Números de punto flotante, es decir los decimales
# los números decimales se separan con punto en python
# precio_producto = 15.34

# Texto(cadenas de caracteres)
# nombre1 = "Jorge"
# nombre2 = "Enrique"
# print(nombre1 + ", " + nombre2)# esto nos devolverá (Jorge, Enrique)

# Booleanos(verdadero y falso)

# mayor_de_edad = True
# print(mayor_de_edad)
# trabaja = False
# print(trabaja)

#* 5 Convertir un dato a un tipo diferente

# n1 = input("Escribe un número: ")# Esto nos pedirá ingresar un número y luego al 
# #llamar a la variable nos devolvera el número ingresado como un string.
# n2 = input("Escribe un número: ")

# n1 = int(n1)# con esto convertimos el valor de la variable n1 a entero.
# n2 = int(n2)#convertimso el string de n2 a entero
# print(n1 + n2) # ahora si podríamos sumar ambos números

# numero_decimal = 4.5
# print(int(4.5)) # con est convertimos un número decimal a entero

# # Si queremos convertir un número a un string hacemos lo siguiente
# str(numero_decimal)# con esto convertimos un número a un string con la función str
# print(numero_decimal)

#* 6 Operadores lógicos de comparación (and, or, not)

# es_estudiante = True
# trabaja = False
# # operadores lógicos

# es_estudiante and trababa # si ahcemos uso del operador and, todas las variables deben ser verdaderas, de lo cntrario nos mostrarpa false
# es_estudiante or trababa # en este caso nos dará verdadero pues una de las dos variables es verdadera, solo devolcverá falso cuando el contenido de todas las variables sea falso
# not es_estudiante # con el operador not, lo que hacemos es invertir el valor de una variable, si es true será false y si es false será true

# operadodes de comparación (==, !=, >,<, >=, <=)

# numer1 = 5
# numer2 = 5
# numer3= 7
# # con el operador de doble igual(==) comparamos el valor de ambas variables
# print(numer1==numer2)# este será true
# print(numer1==numer3)# este será false

# # con el operador distinto (!=) preguntamos si el valor de una variable es distinto de otra
# print(numer1!=numer3)#esto será true
# print(numer1!=numer2)#esto será false

# # con el operdor mayor y menor (>, <, >=,<=) podemos comparar los valores de las varibles y determinar si uno es mayor, menor, mayor igual y menr igual
# print(numer1>numer3) # esto será false
# print(numer1>=numer2) # esto será verdadero
