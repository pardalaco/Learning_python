"""for i in [1,"2",3]:#For + variable + in + numero de nombres en una lista, tupla... La variable (i) es igual a 1 en la primera vuelta, 2 en la segunda...
	print(i)"""

"""for i in ["Pildoras", "Informaticas", 3]:

	print("Hola", end=" ")#La funcion end lo que hace es que se escriba todo en la misma linea"""

"""email=False
n1=input("Introduzca su email: ")


for i in "Danirovira03@gmail.com":#se escribira las veces como caracteres tenga
	if(i=="@"):
		email=True
if email:#Aun que no pongamos email==True si ponemos solo el nombre de la variable es como si se lo estubieramos diciendo
	print("El email es correcto")
else:
	print("El email no es correcto")"""



""""for i in range(5):#Lo que hace rangen en python tres es un tipo, hace que se repita 5 veces  0,1,2,3,4
	print(i )"""


contador1=0
contador2=0
miEmail=input("Introdu tu email: ")


for i in miEmail:#se escribira las veces como caracteres tenga
	if(i=="@"):
		contador1=contador1+1

	elif(i=="."):
		contador2=contador2+1

if contador1>=2 or contador2==0:#Aun que no pongamos email==True si ponemos solo el nombre de la variable es como si se lo estubieramos diciendo
		print("El email es incorrecto")

else:
	print("El email es correcto")