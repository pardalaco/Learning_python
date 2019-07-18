#Todo el codigo esta bien pero si ponemos a dividir un numero por un cero el programa se rompe


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try:#si nos da el codigo error, podemos poner un try y si el codigo funciona continuara normal
		return num1/num2
	
	except ZeroDivisionError:#Si el codigo no ha funcionado en el try entonces se ejecutara el ecept (para poner un except tenemos que poner el ecept y el error)
		print("No se puede dividir entre 0")#Despued del escept ponemos lo que el codigo que queremos que se eccecute en este caso un print
		return "Operacio+n erronia"

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")