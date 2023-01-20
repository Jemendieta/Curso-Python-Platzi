# Juego de  piedra, papel o tijera
import os
os.system("cls")

eleccion =input("ingresa tu elección: " )

if eleccion == "papel" or eleccion == "Papel":
  print("la PC elige tijera, gana la PC...😁")
elif eleccion == "piedra" or eleccion == "Piedra":
  print("la PC elige papel, gana la PC..😁")
elif eleccion == "tijera" or eleccion == "Tijera":
  print("la PC elige piedra, gana la PC...😁")
else:
  print("elige una opción correcta...🤨")