import math

def calculaRiz(num1):
	if num1<0:
		raise ValueError("El numero no puede ser negativo")

	else:
		return math.sqrt(num1)

op1=(int(input("Inroduce un numero: ")))
try:
	print(calculaRiz(op1))

except ValueError as ErrorDeNumeroNegativo:#Tenemos que capturar la variable que emos echo saltar antes "Linia 5" y con el as hemos asignado el ErrorDeNumeroNegativo.

	print(ErrorDeNumeroNegativo)

print("Programa finalizado")