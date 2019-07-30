from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)# Especificamos que el frame estara en la raiz (root)

miFrame.pack()

miImagen=PhotoImage(file="matrix.gif")# Dentro del parentesi ponemos file="La ruta de la imagen"

Label(miFrame, image=miImagen).place(x=100, y=200)

#miLabel=Label(miFrame, text="Hola gente", fg="blue", font=("Comic Sasns MS", 18))#Podemos poner mas de una propiedad al Label // dentro de la fuente podemos cambiar el tipo de letra y el tamano

#miLabel.pack()# Si lo empaquetamos a la hora de ejecutarlo nos redimensiona la ventana

#miLabel.place(x=100, y=200)# Esta funcion lo que hace es le podemos indicar unas cordenadas x e y (La medida es en pixeles) 

#Label(miFrame, text="Hola gente").place(x=100, y=200)# Si no vamos a usar otra vez la variable miLabel podemos simmplificar el texto de esta manera

root.mainloop()