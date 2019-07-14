#and: y ademas
#or: o sino/o si nada de lo anterior es cierto
#in

print("Programa de becas 2019")

Distancia_escuael=int(input("Introduce la distancia a la escuela: "))
print(str(Distancia_escuael) + "km")

Numero_hermanos=int(input("Introduce el numero de hermanos: "))
print(Numero_hermanos)

salario_familiar=int(input("Introduce el salario familiar bruto: "))
print(salario_familiar)


if Distancia_escuael>=40 and Numero_hermanos>=2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")