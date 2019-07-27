"""import pickle

list_nombres=["Peddro", "Ana", "Maria", "Isabel"]

fichero_binario=open("list_nombres", "wb")#Nombre del fichero + escritura "W" binaria "b"

pickle.dump(list_nombres, fichero_binario)#Dump sirve para bolcar la lista, variable ... dentro del archivo y le tenemos que poner la lista  y el segundo argumento que temnemos que poner es el nombre del fichero que queremos bolcar

fichero_binario.close()

del (fichero_binario)#La funcion del sirve para borrarlo de la memoria"""

import pickle

fichero=open("list_nombres", "rb")#Read binari(rb) esta funcion sirve para que pueda leer el codigo binario

lista=pickle.load(fichero)#Utilizamos el metodo load para cargar la informacion que tenemos almacenada en fichero

print(lista)