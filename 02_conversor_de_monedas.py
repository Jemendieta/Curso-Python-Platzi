#* PROGRAMA PARA CONVERTIR MONEDAS - SOLES A DOLARES

# soles = input("¿Cuántos soles quieres convertir?: ")
# soles = float(soles)#con float convertimos el valor de soles a decimal
# valor_dolar = 3.75
# dolares = soles / valor_dolar
# dolares = round(dolares, 2) # con round redondeamos el valor de una varaible y el número 2 representa la cantida de decimales que queremos
# dolares = str(dolares)#convertimos el valor de dolares a string
# print("Tienes $" + dolares + " dolares")

#* CONVERTIR DOLARES A SOLES

# dolar = input("¿Cuántos dolares quieres convertir?: ")
# dolar = float(dolar) # convertimos el valor a decimal
# valor_sol = 3.75
# sol = dolar * valor_sol
# sol = round(sol, 2)
# sol = str(sol)# convertimos a string
# print("Tienes S/ "+ sol + " soles")

#* MONEDAS DE VARIOS PAISES

# escribiendo tres pares de comillas dobles podemos colocar varias lineas string
# menu = """
# Bienvenido al conversor de momedas de Python 🤑💲🤑💲🤑

# 1 - Pesos Colombianos
# 2 - Pesos Mexicanos
# 3 - Soles Peruanos

# Elige una opción: """

# opcion = input(menu)

# if opcion=="1":
#   pesos = input("¿Cuántos pesos Colombianos quieres convertir?: ")
#   pesos = float(pesos)
#   valor_dolar = 3875
#   dolares = pesos / valor_dolar
#   dolares = round(dolares,2)
#   dolares = str(dolares)
#   print("Tienes $ " + dolares + " dólares")
# elif opcion=="2":
#   pesos = input("¿Cuántos pesos Mexicanos quieres convertir?: ")
#   pesos = float(pesos)
#   valor_dolar = 19.81
#   dolares = pesos / valor_dolar
#   dolares = round(dolares,2)
#   dolares = str(dolares)
#   print("Tienes $ " + dolares + " dólares")
# elif opcion=="3":
#   soles = input("¿Cuántos soles Peruanos quieres convertir?: ")
#   soles = float(soles)
#   valor_dolar = 3.75
#   dolares = soles / valor_dolar
#   dolares = round(dolares,2)
#   dolares = str(dolares)
#   print("Tienes $ " + dolares + " dólares")
# else:
#   print("ingrese una opción entre 1 y 3")

#* Realizaremos el mismo ejercicio pero ahora con funciones para modularizar nuestro programa

def conversor(tipo_moneda, valor_dolar):
  pesos = input("¿Cuántos pesos " + tipo_moneda + " quieres convertir?: ")
  pesos = float(pesos)
  dolares = pesos / valor_dolar
  dolares = round(dolares,2)
  dolares = str(dolares)
  print("Tienes $ " + dolares + " dólares")

menu = """
Bienvenido al conversor de momedas de Python 🤑💲🤑💲🤑

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Argentinos

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
  conversor("Colombianos", 3875)
elif opcion == 2:
  conversor("Mexicanos",19.81)
elif opcion == 3:
  conversor("Argentinos", 65)
else:
  print("Elige una opción válida")

numeroA = 3
numeroB = 4

