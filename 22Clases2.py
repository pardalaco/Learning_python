class Coche():

	def __init__(self):#Hemos creado un constructor

		self.__largoChasis=250 # Las propiedades tienen que estar dentro de el metodo constructor precedidas por la palabra self
		self.__anchoChasis=120
		self.__ruedas=4 # Hemos encapsulado una clase entonces no sera accesible desde fuera de la clase(modificar desde fuera) pero si que es accesible desde dentro de la clase
		self.__enMarcha=False

	def arrancar(self,arrancamos):#Un metodo es una funcion especial que pertenece a la clase // self hace referencia a la instancia de la clase//Tambien le hemos anadido el parametro arrancar
		self.enMarcha=arrancamos

		if(self.enMarcha):
			return("El coche esta en marcha")


		else:
			return("El coche esta parado")


		self.enMarcha=True # Hemos echo que se ponga en marcha, hemos canviado una propiedad que venia por defecto

	def estado(self):
		print("El coche tiene ", self.__ruedas," ruedas. Un ancho de: ", self.__anchoChasis, ". Y un largo de:",
			self.__largoChasis)


miCoche=Coche() # Hemos echo instanciacion de una clase

#print("El largo del coche es: ", miCoche.largoChasis)#Propiedad (Coche) + caracteristica (largoChasis) y hace falta la coma para encadenar el texto don lo demas
#print("El coche tiene: ", miCoche.ruedas  ," ruedas")
print(miCoche.arrancar(True))#El self se almacena en miCoche y cambia la propiedad (Al poner esta funcion arrancamos el cohe, porque activamos la funcion arrancar)

print(miCoche.estado())#Nos muestra el estado del coche

print("-------A continuacion creamos el siguiente objeto----------")

miCoche2=Coche()

#print("El largo del coche es: ", miCoche2.largoChasis)
#print("El coche tiene: ",miCoche2.__ruedas," ruedas")
print(miCoche2.arrancar(False))#El true o false se almacena en arrancamos, por eso arranca o no

miCoche2.ruedas=2 # Estamos intentando modificar la propiedad

print(miCoche2.estado())
