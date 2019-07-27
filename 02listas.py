#!/usr/bin/python3
# -*- coding: utf-8 -*-

miLista=["María", 2, True, 112.2, "Antonio"]
#Crea una lista
#La lista se numera: 0,1,2,..

miLista.extend(["Sandra", "Anna", "Lucia"])
#Anade elementos al final de la lista

print(miLista[:])
#Pinta la lista

print(miLista[2:4])
#Pinta del 2 al 4

miLista.append("Cristina")
print(miLista[:])
#Agrega un nombre al final de la lista


print(miLista.index("María"))
#Busca la primara posicion del nombre

print("Pepe" in miLista)
#Busca si esta ese nombre en la lista y lo marca con True o Folse

miLista.remove("Anna")
print(miLista[:])
print(miLista[6])
#Quita el nombre de la lista

miLista.pop()
print(miLista[:])
#Quita el ultimo nombre de la lista


miLista2=["Sandra", "Lucía"]
miLista3=miLista+miLista2
print(miLista3[:])
#Junta dos listas

miLista=["María", 2, True, 112.2, "Antonio"]*3
print(miLista[:])
#Escribe la lista por el numero indicado (en este caso 3), [la multiplica]
