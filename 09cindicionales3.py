print("Asignaturas obtativas año 2019")
print("Asignaturas obtativas: Informática gráfica - Pruebas de sofware - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()#Passa todas las letras a minuscula, para poder escribir las asignaturas en minuscula

if asignatura in ("informática gráfica", "pruebas de sofware", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no está en la lista")