def divide():
	
	try:

		op1=(float(input("Introduce el primer numero: ")))#En vez de int ponemos float para poder trabajar con decimales
		
		op2=(float(input("Introduce el segundo numero: ")))

		print("La division es: " + str(op1/op2))

	#Si ponemos un except: captura una esseccion general

	except ValueError:
		print("El valor introducido es erroneo")

	except ZeroDivisionError:
		print("No se puede entre por 0")

	finally:#Con esto lo que hacemos es que siempre se ejecute esa linea de codigo

		print("Calculo finalizado")

divide()