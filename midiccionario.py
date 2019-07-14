print("Programa de evaluacion de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")

def posible(numero):
	existente="Existe"
	if numero>10:
		inexistente="No existe"
		print(inexistente)
	return existente
	

posible(int(nota_alumno))

def evaluacion(nota):
	valoracion="aprovado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
print(evaluacion(int(nota_alumno)))