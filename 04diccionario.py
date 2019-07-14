midiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino unido":"Londres", "Espana":"Madrid"}
print(midiccionario["Francia"])
#Creamos un cicionario ("clave":"valor que le damos a la clave",)

midiccionario["Italia"]="Lisboa"
print(midiccionario)
#Anadimos una variable mas

midiccionario["Italia"]="Roma"
print(midiccionario)
#Sobreescribimos el valor para cambiarlo, (Nunca la misma clave puede tener dos valores)

del midiccionario["Reino unido"]
print(midiccionario)
#Eliminamos el elemento seleccionado

midiccionario1={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario1)
#Convinaciones varias

mitupla=["Espana", "Francia", "Reino unido", "Alemania"]
midiccionario2={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario2)
#Asignamos a la tupla valores dentro del diccionario

midiccionario3={23:"Jordan", "nombre":"Michel", "Equipo":"Chicago", "Anillos":[1991,1993,1996,1997,1998]}
print(midiccionario3["Anillos"])
#Como no se pueden asignar dos valores a la misma clabe, lo que hacemos es asignar una tupla

midiccionario3={23:"Jordan", "nombre":"Michel", "Equipo":"Chicago", "Anillos":{"tenporadas":[1991,1993,1996,1997,1998]}}
print(midiccionario3["Anillos"])
#Creamos un diccionario dentro del diccionario

print(midiccionario3.keys())
#Imprime las llabes

print(midiccionario3.values())
#Imprime los valores

print(len(midiccionario3))
#Como de largo es el diccionario