#El programa funciona pero solo en terminal

"""def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilvao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))"""

def devuelve_ciudades(*ciudades):#Cuando colocamos un asterisco delante de un elemento de una funcion le decimos que los elementos que va a recibir los recivira en forma de tupla
	for elemento in ciudades:
		
		"""for subElemento in elemento:

			yield subElemento"""

		yield from elemento #yield from nos permite prescindir del bucle for anidado

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilvao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))