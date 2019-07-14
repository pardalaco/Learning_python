#if: si
#else: y si no es verdad

"""print("Verificavion de acceso")

edad_usuario=int(input("Introducce tu edad, porfa vor: "))

if edad_usuario<18:
	print("No puede pasar")
elif edad_usuario>120:#Elif es como un "else" pero en ocaciones que necesitemos 3 o mas else
	print("Edad incorrecta")
else:
	print("Puedes pasar")
print("El programa ha finalizado")"""

print("Verificavion de acceso")

nota_alumno=int(input("Introducce tu nota, porfa vor: "))

if nota_alumno<5:
	print("Insuficiente")
elif nota_alumno<6:
	print("Suficiente")
elif nota_alumno<7:
	print("Bien")
elif nota_alumno<9:
	print("Notable")
else:
	print("Sobresaliente")