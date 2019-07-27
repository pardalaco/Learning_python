"""1r fase: Creacion
2n fase: Apertura
3 fase: Manipulacion
4 fase: Cierre
"""

# -*- coding: utf-8 -*-

"""from io import open

archivo_texto=open("archivo.txt", "w")#Le pedimos el argoumento que lo vamos a abrir y el modo en que lo vamos a abrir (lo podemos abrir en modo: lectura, escritura y appen) // la w es de write (escritura)//  Lo que ha hecho open es abrir el archivo pero como no habia ningun archivo lo a creado

frase=(("Estupendo dia para estudiar python /n Hoy es Jueves").decode('unicode_escape'))

archivo_texto.write(frase)#Hemos dicho que nos escriba la variable "Frase"

archivo_texto.close()# Cerramos el archivo que hemos escrito en memoria con nuestro programa python#Esto seria apra tenerlo en modo escritura"""

"""from io import open

archivo_texto=open("archivo.txt", "r")

texto=archivo_texto.read()# Tambien podemos utilizar la funcion readlines (lo que hace es leer lo que hay almacenado dentro del archibo linea a linea y lo almacena en una lista) 

archivo_texto.close()

print(texto)"""

"""from io import open

archivo_texto=open("archivo.txt", "r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[:])"""

"""from io import open

archivo_texto=open("archivo.txt", "a")# La a es de append lo abre en modo extension o anadir

archivo_texto.write("/n siempre es una buena ocasion para estudiar python")

archivo_texto.close()"""

"""from io import open

archivo_texto=open("archivo.txt", "r")

archivo_texto.seek(11)# Le estamos diciendo que le cursor se situe el el puesto 11 // al leer el archivo por defecto se situaria al final // ca a enpezar a leer en la posicion 11 entonces los 10 primeros caracteres no los va a leer

print(archivo_texto.read(20))# Le podemos indicar a read que haga una lectura hasta el caracter 20

print(archivo_texto.read(20))"""

"""from io import open

archivo_texto=open("archivo.txt", "r")

archivo_texto.seek(len(archivo_texto.read())/2)

print(archivo_texto.read())"""

from io import open

archivo_texto=open("archivo.txt", "r+")#Es de lectura y escritura

lista_texto=archivo_texto.readlines()

lista_texto[1]=" Esta linea ha sido incluidad desde el exterior \n"

archivo_texto.seek(0)

#archivo_texto.writelines(lineas_texto)

archivo_texto.close()