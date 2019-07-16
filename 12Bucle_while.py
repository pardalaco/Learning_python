#while: mientras
"""
i=1

while i <=10:
	print("Ejecucion" + str(i))#La funcion str lo que hace es convertir el int en texto asi para poder poner la cariable en el print
	i=i+1

print("Termino la ejecucion")"""

edad=int(input("Introduce la edad: "))

while edad<0 or edad>100:
	print("Has intrducido una edad incorrecta, vuelve a intentarlo")
	edad=int(input("Introduce la edad: "))

 
print("Tienes " + str(edad) + " anos")