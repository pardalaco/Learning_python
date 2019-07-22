opcion1=int(input("Introduce el primer signo: "))
opcion2=int(input("Introduce el segundo signo: "))


def adivina(opcion1, opcion2):
	if opcion1 and opcion2=="+"and"+":
		print ("Es positivo")

	elif opcion1 and opcion2=="+"and"-":
		print("Es negativo")

	else:
		print("Es negativo")

print("Ek orograma ha finalizado")