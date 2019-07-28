from tkinter import *

raiz=Tk()#Creamos una variable y utilizamos la clase Tk

raiz.title("Ventana de pruebas")#Le pone nombre a la ventaqna y aparece en la parte superior

raiz.resizable(1,1)#Esta variable es de tipo buleano (0,1), (True, False). El primero corresponde al ancho (width) y el segundo al alto (height) y le estamos diciendo que no se redimensione ni a lo ancho ni a lo alto (False, False)

#raiz.iconbitmap("slash.ico")#raiz.nombre del objeto(ruta del objeto)

#raiz.geometry("650x350")# Esta funcion sirve para definir la ventana

raiz.config(bg="blue")#bg es background raiz.config(bg="color en ingles")

miFrame=Frame()

#miFrame.pack(side="right", anchor="n")#Esto sirve para empaquetar el frame // side sirve para anclarlo // anchor sirve para anclar el frame a dos sitios al mismo tiempo y la n significa norte

#miFrame.pack(fill="x")# Fill sirve para rellenarlo //El frame se redimensiona con la raiz orizontalmente

#miFrame.pack(fill="y", exmpand="True")#Para que se espanda verticalmente a parte de poner fill="y" tambien hay que activar el expand con un True

#miFrame.pack(fill="both", expand="True")#Both sirve para que se redimensione vertical y orizontalmente

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650", height="350")# Configuramos el frame para que tenfa un alto (width) y un ancho (height)

miFrame.config(bd=35)#bd significa borde

miFrame.config(relif="sunken")#Con la funcion relif le indicamos que ponga un tipo de borde

miFrame.config(cursor="hand2")#Esto sirce para cambiar de pulsor

raiz.mainloop()#Esta opcion sirve para que el programa este a la escucha de lo qeu hace el usuario, por lo tanto esta en un bucle infinito. Este metodo siempre tiene que estar en ultimo lugar
"""Para que te salga el icono deseado tienes que tener en la misma carpeta del programa una extension .icon

Hemos aplicado bordes y cambios de cursor al raton cuandoe sta encima de frame pero esto tembien podemos hacerlo con la raiz

"""