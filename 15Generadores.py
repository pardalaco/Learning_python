#Lo que hace yield es generar el valor en el momento que lo necesite y si no lo necesita se queda en un estado de reposo hasta que buelve a pedirle otro valor

"""def genera_pares(limite):

	num=1

	miLista=[]

	while num<limite:
		miLista.append(num*2)
		num+=1

	return miLista

print(genera_pares(10))"""#La lista lo nos ha creado nueve numeros pares

def genera_pares(limite):

	num=1

	while num<limite:

		yield num*2
		
		num+=1

devuelve_pares=genera_pares(10)

print(next(devuelve_pares))#Nos devuelveel primer valor que tiene almacenado en su interior

print("Aqui podria ir mas codigo")
print(next(devuelve_pares))

print("Aqui podria ir mas codigo")
print(next(devuelve_pares))
