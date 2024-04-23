import random
import time
import os


def print_title(title):
    width =  30
    print("*" * width)
    print("*", title, "*")
    print("*" * width)

print_title("Batalla Naval")
time.sleep(2)

while True:
 opcion=input("inserte 'START' para comenzar: ").upper()
 if opcion=="START":
     break
 else:
     print("valor invalido, inserte 'START' para comenzar: ")


time.sleep(1)
print_title("Registro De Jugadores")
time.sleep(2)

jugador1 = {}
jugador2 = {}
while True:
    jugador1_nombre = input("Insertar el nombre para el jugador 1: ").capitalize()
    jugador1_alias = input("Insertar el alias para el jugador 1: ")
    jugador2_nombre = input("Insertar el nombre para el jugador 2: ").capitalize()
    jugador2_alias = input("Insertar el alias para el jugador 2: ")
    
    if (jugador1_nombre == jugador1_alias or jugador2_nombre == jugador2_alias):
        print("Nombre y alias son iguales, por favor ingresar uno distinto.")
    elif (jugador1_nombre == jugador2_nombre or jugador1_alias == jugador2_alias):
        print("Nombre en uso. Por favor, introduce nombres y alias diferentes.")
    else:
        jugador1[jugador1_nombre] = jugador1_alias
        jugador2[jugador2_nombre] = jugador2_alias
        break

print(jugador1)
print(jugador2)
