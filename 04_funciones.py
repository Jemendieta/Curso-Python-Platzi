#*  FUNCIONES EN PYTHON
# Estas nos permiten ahorrar líneas de código, principalmente donde tenemos secuencias que se repiten
# para declarar funciones lo hacemos medianrte la palabra reservada def
# def imprimir_mensaje():
#   print("Aprendiendo funciones en Python")
#   print("Aprendiendo Python")

# imprimir_mensaje()# de estoa forma invocamos una función en Python

#* Trabajando con parámetros

# def conversacion(mensaje):
#   print("hola")
#   print("¿Cómo estás?")
#   print(mensaje)
#   print("Adios")

# opcion = int(input("Elige una opción (1, 2, 3): "))
# if opcion == 1:
#   conversacion("Elegiste la opción 1")
# elif opcion == 2:
#   conversacion("Elegiste la opción 2")
# elif opcion == 3:
#   conversacion("Elegiste la opción 3")
# else:
#   print("Escribe una opción correcta")

#* Ejercicio de suma

def suma(a,b):
  print("Se suman dos números")
  resultado = a + b
  return resultado # con return, devolvemos la variable resultado

sumatoria = suma(1,4)
print(sumatoria)