from tkinter import *

raiz=Tk()#Creamos una variable y utilizamos la clase Tk

raiz.title("Ventana de pruebas")#Le pone nombre a la ventaqna y aparece en la parte superior

raiz.resizable(0,0)#Esta variable es de tipo buleano (0,1), (True, False). El primero corresponde al ancho (width) y el segundo al alto (height) y le estamos diciendo que no se redimensione ni a lo ancho ni a lo alto (False, False)

#raiz.iconbitmap("slash.ico")#raiz.nombre del objeto(ruta del objeto)

raiz.geometry("650x350")# Esta funcion sirve para definir la ventana

raiz.config(bg="blue")#bg es background raiz.config(bg="color en ingles")

raiz.mainloop()#Esta opcion sirve para que el programa este a la escucha de lo qeu hace el usuario, por lo tanto esta en un bucle infinito. Este metodo siempre tiene que estar en ultimo lugar
"""Para que te salga el icono deseado tienes que tener en la misma carpeta del programa una extension .icon"""