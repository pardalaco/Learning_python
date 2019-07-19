def evlualuaEdad(edad):

	if edad<0:
		raise TypeError("No se permiten valores negativos")#La funcion raise lo que hace es sacarnnos una excepcion dentro del programa

	if  edad<20:
		return "Eres muy joven"

	if edad<40:
		return "Eres joven"

	if edad<65:
		return "Eres maduro"

	if edad<100:
		return "Eres anciano"

print(evlualuaEdad(-18))