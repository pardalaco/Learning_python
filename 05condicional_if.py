def evaluacion(nota):#Funcion para ver si el alumno esta aprobado
	valoracion="aprovado"#Variablae
	if nota<5:#Mayor que 5 esta aprobado. Hay varios cvalores: <mayor qeu, >menor que, ==igual que, >=menor o igual que, <mayor o igual que, !=diferente que
		valoracion="suspenso"#Si no es mayor que 5 estara suspendido
	return valoracion#Nos debuelve la variable (Es necesario que nos la devuelva o no funcionara)
#print(evaluacion(5))


print("Programa de evaluacion de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")#Input es la funcion que nos permite escribir en la terminal(por diefecto se introduce el input como "texto") Tambien se pueden escribir parametros dentro de la funcion imput

def evaluacion(nota):
	valoracion="aprovado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
print(evaluacion(int(nota_alumno)))#La funcion int transforma en numero entero el nombre introducido
