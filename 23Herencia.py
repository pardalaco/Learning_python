class Veiculos():

	def __init__(self, marca, modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		
		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frena(self):
		
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		 self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)#Poniendo "\n" lo que hacemos es un salto de linia.

class Moto(Veiculos):#Dentro de la clase ejos heredado la herencia veiculos
	pass

miMoto=Moto("Honda", "CBR")#Le indicamos la marca y el modlo (Linia 3)

miMoto.estado()