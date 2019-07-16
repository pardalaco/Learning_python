""""for letra in "Python":

	if letra=="h":
		continue#Esta funcion le esta diciendo al codigo que salte la condicion que le hayamos puesto

	print("Viendo la letra: "+ letra)"""

"""nombre="Pildoras informaticas"

contador=0

for i in nombre:

	if i==" ":
		continue

	contador+=1#Eso es lo mismo que contador=contador+1

print(contador)"""

email=input("Introduce tu email: ")

for i in email:

	if i=="@":

		arroba=True

		break;

else:
	arroba=False

print(arroba)