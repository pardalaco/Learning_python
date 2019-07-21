class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

	def arrancar(self): # Un metodo es una funcion especial que pertenece a la clase // self hace referencia a la instancia de la clase
		self.enMarcha=True # Hemos echo que se ponga en marcha, hemos canviado una propiedad que venia por defecto

	def estado(self):
		if (self.enMarcha):
			return ("El coche esta en marcha")

		else:
			return("El coche esta parado")

miCoche=Coche()# Hemos echo instanciacion de una clase

print("El largo del coche es: ", miCoche.largoChasis) # Propiedad (Coche) + caracteristica (largoChasis) y hace falta la coma para encadenar el texto don lo demas
print("El coche tiene: ",miCoche.ruedas," ruedas")
miCoche.arrancar() # El self se almacena en miCoche y cambia la propiedad (Al poner esta funcion arrancamos el cohe, porque activamos la funcion arrancar)

print(miCoche.estado()) # Nos muestra el estado del coche

print("A continuacion creamos el siguiente objeto")

miCoche2=Coche()

print("El largo del coche es: ", miCoche2.largoChasis)
print("El coche tiene: ",miCoche2.ruedas," ruedas")

print(miCoche2.estado())
