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

# def conversor(tipo_moneda, valor_dolar):
#   pesos = input("¿Cuántos pesos " + tipo_moneda + " quieres convertir?: ")
#   pesos = float(pesos)
#   dolares = pesos / valor_dolar
#   dolares = round(dolares,2)
#   dolares = str(dolares)
#   print("Tienes $ " + dolares + " dólares")

# menu = """
# Bienvenido al conversor de momedas de Python 🤑💲🤑💲🤑

# 1 - Pesos Colombianos
# 2 - Pesos Mexicanos
# 3 - Pesos Argentinos

# Elige una opción: """

# opcion = int(input(menu))
# if opcion == 1:
#   conversor("Colombianos", 3875)
# elif opcion == 2:
#   conversor("Mexicanos",19.81)
# elif opcion == 3:
#   conversor("Argentinos", 65)
# else:
#   print("Elige una opción válida")

# numeroA = 3
# numeroB = 4

# ahora haremos un ejemplo con fstrings
# import os
# os.system('cls')

# USD = 1
# ARS = 290
# COP = 4600
# MXN = 20
# PEP = 3.50

# print("Bienvenido al conversor de monedas")
# print("Elige una de las siguietes opciones de conversión: ")
# print("1 - Dolares estadounidenses a pesos argentinos")
# print("2 - Dolares estadounidenses a pesos colombianos")
# print("3 - Dolares estadounidenses a pesos mexicanos")
# print("4 - Dolares estadounidenses a soles peruanos")

# opcion = int(input("¿Cuál es tu opción?"))

# if opcion == 1:
#   dolares = int(input("¿Cuántos dolares tienes?: "))
#   moneda = dolares * ARS
#   print(f"Tienes {moneda} pesos")
# elif opcion == 2:
#   dolares = int(input("¿Cuántos dolares tienes?: "))
#   moneda = dolares * COP
#   print(f"Tienes {moneda} pesos")
# elif opcion == 3:
#   dolares = int(input("¿Cuántos dolares tienes?: "))
#   moneda = dolares * MXN
#   print(f"Tienes {moneda} pesos")
# elif opcion == 4:
#   dolares = int(input("¿Cuántos dolares tienes?: "))
#   moneda = dolares * PEP
#   print(f"Tienes {moneda} soles")
# else:
#   print("Elige una opción correcta...🤨")


# Conversor de pesos a dolares
ARS = 290
COP = 4600
MXN = 20
PEP = 3.50

print("Bienvenido al conversor de monedas")
print("Elige una de las siguietes opciones de conversión: ")
print("1 - Pesos argentinos a dolares estadounidenses")
print("2 - pesos colombianos a dolares estadounidenses")
print("3 - Pesos mexicanos a dolares estadounidenses")
print("4 - Soles peruanos a dolares estadounidenses")

opcion = int(input("¿Cuál es tu opción? "))

if opcion == 1:
  moneda = int(input("¿Cuántos pesos tienes?: "))
  dolares = moneda / ARS
  print(f"Tienes {dolares} dolares")
elif opcion == 2:
  moneda = int(input("¿Cuántos pesos tienes?: "))
  dolares = moneda / COP
  print(f"Tienes {dolares} dolares")
elif opcion == 3:
  moneda = int(input("¿Cuántos pesos tienes?: "))
  dolares = moneda / MXN
  print(f"Tienes {dolares} dolares")
elif opcion == 4:
  moneda = int(input("¿Cuántos soles tienes?: "))
  dolares = moneda / PEP
  print(f"Tienes {dolares} dolares")
else:
  print("Elige una opción correcta...🤨")