import math#hemos importado esa clase con todas sus funciones que le acompanan

print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	if(intentos==2):
		print("Has consumido demasiados intentos, el programa ha finalizado")
		break;#Lo que hace break es si el programa lo llega a leer el bucle termina

	numero=int(input("Introduce un numero: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)#Introducimos la clase math y el sqrt lo que dice es raiz cuadrada de(...)
	print("La raiz cuadrada de " + str(numero) +  " es " + str(solucion))