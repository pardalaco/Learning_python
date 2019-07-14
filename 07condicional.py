"""edad=-7

if 0<edad<100:#Lo que hacemos es decirle que el numero sera correcto si es mayor que 0 pero menor que 100
	print("La edad es corecta")
else:
	print("Edad es incorrecta")"""


salario_presidente=int(input("Introduce el salario del presidente: "))
print("Este es el salario del presidente" + str(salario_presidente))#La funcion str lo que hace es convertir el int en texto asi para poder poner la cariable en el print

salario_director=int(input("Introduce el salario del director: "))
print("Este es el salario del director" + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe del area: "))
print("Este es el salario del jefe del area" + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Este es el salario del administrativo" + str(salario_administrativo))


if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")


