import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una personas nueva con el nombre: ", self.nombre )

	def __str__(self):#La funcion str es convertir en cadena de texto la informacion de un objeto

		return"{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas(object):
	
	personas=[]

	def __init__(self):
		listaDePersonas=open("FicheroExterno", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))#{}Son el numero de personas que hemos puesto


		except:
			print("El fichero esta vacio")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()


	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("FicheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()

	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)


miLista=listaPersonas()


persona=Persona("Ana", "Femenino", 19)

miLista.agregarPersonas(persona)

miLista.mostrarInfoFicheroExterno()