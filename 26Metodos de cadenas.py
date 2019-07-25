"""http://pyspanishdoc.sourceforge.net/lib/typesseq.html
Aqui estan todos los metodos de las cadenas"""


nombreUsuario=input("Introduce un nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())#Los metodos se utilizaban poniendo = objeto.metodo, en este caso lo estamos pasando todo a mayusculas
print("El nombre es: ", nombreUsuario.lower())#Ponemos todo el nombre en minuscula
print("El nombre es: ", nombreUsuario.capitalize())#Ponemos la primera letra en mayuscula

edad=input("Introduce la edad: ")

print(edad.isdigit())#Comprueba con true o folse si es un numero

while (edad.isdigit()==False):
	
	print("Pirfabor introduce un valor numerico")

	edad=input("Introduce la edad: ")
	
for (int(edad) <18):
	print("No puedes pasar")

else:
	print("Puedes pasar")