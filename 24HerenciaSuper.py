#El programa no funciona
class Persona():

	def __init__ (self, nombre, edad, Lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=Lugar_residencia

	def descripcion(self):
		
		print("Nombre: ", self.nombre, " Edad: ", self.edad, " Lugar de residencia: ", self.lugar_residencia)

class Empleado(Persona):#Si aplicamos por el principio de substitucion es siempre un/a (Un empleado es siempre una persona)

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)#La funcion super llama al metodo de la clase padre

		self.salario=salario
		self.antiguedad=antiguedad
		
	def descripcion(self):
		super().descripcion()


		print (" Salario: ", self.salario, "Antiguedad: ",  self.antiguedad)

Manuel=Empleado(1500, 15, "Manuel", 55, "Xativa")#Primero asignamos los valores de la clase y despues los de super(La herencia)

Manuel.descripcion()

print(isinsta(Manuel, Empleado))#Esto es para comprobar si manuel pertenece a la clase empleado y nos deve de devolver true o false

