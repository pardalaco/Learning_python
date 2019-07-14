#Por el contrario de las listas, las tuplas no se puede hacer: extend, append, remove
#Las tuplas no se pueden alterar como las listas

miTupla=("Juan", 13,1,1995)
print(miTupla[:])
#Crea una tupla

milista=list(miTupla)
print(milista[:])
#hemos comvertido la tupla en lista

milista1=["Jose", 12, 123, 12]
miTupla1=tuple(milista1)
print(miTupla1)
#hemos comvertido la lista en una tupla

print("Juan" in miTupla)
#Busca si esta ese nombre en la tupla y lo marca con True o False

print(miTupla.count(13))
#Mira cuantas veces esta ese nombre en la tupla

print(len(miTupla))
#Longitud de la tupla (cuantos elementos se encuentran dentro)

miTupla2=("Juanito",)
print(len(miTupla2))
#tupla unitaria (de un unico elemento)

miTupla4="Pedrin", 12, 432, 234
print(miTupla4)
#Tupla sin parentesis, las tuplas se pueden escribir con o sin parentesis (empaquetado de tupla)

miTupla=("Juan", 13,1,1995)
nombre, dia, mes, ano=miTupla
print(nombre)
print(dia)
print(mes)
print(ano)
#(Desempaquetado de tupla) asigna los valores de la tupla a las variables asignadas
