class Coche ():

	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")


"""miVehiculo=Moto()

miVehiculo.desplazamiento()#Estamos utilizando el mismo metodo pero el metodo pertenece a clases diferentes

miVehiculo2=Coche()

miVehiculo2.desplazamiento()

miVehiculo3=Camion()

miVehiculo3.desplazamiento()"""

def desplazamientoVehiculo(Vehiculo):
	Vehiculo.desplazamiento()


miVehiculo=Moto()#Esto esta fuardando la clase camion en miVehiculo

desplazamientoVehiculo(miVehiculo)#Por el polimorfismo (muchas formas) hece que se transforme en un objeto de tipo camion, y esno hace que llame al metodo desplazamiento y que active las funciones anteriores

