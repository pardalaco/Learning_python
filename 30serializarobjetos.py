import pickle

class Vehiculo():

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
		 self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)


coche1=Vehiculo("Fiat", "500")

coche2=Vehiculo("Seat", "srga")

coche3=Vehiculo("Renaut", "sd3")

coches=[coche1,coche2, coche3]

fichero=open("losCoches", "wb")#Creamos o abrimos el fichero

pickle.dump(coches, fichero)#Bolcamos con la funcion dump la lista coches al archivo "fichero"

fichero.close()

del (fichero)

ficheroApertura=open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:

	print(c.estado())