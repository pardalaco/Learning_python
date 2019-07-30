from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()# Le estamos diciendo que la variable minombre es una cadena de caracteres


cuadroNombre=Entry(miFrame, textvariable=minombre)#Con textvariable conseguimos que el cuadro este asociado con el valor de minombre
#cuadroTexto.place(x=100, y=100)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)#Lo que hace esto es dividir el espacio en cuadros para que nos sea mas facil colocar los elementos // con row i column le indicamos donde se tiene que situar
cuadroNombre.config(fg="red", justify="center")#Con la funcion justify le decimos que lo que escriba lo tiene que poner en el "centro", en este caso

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)#Esto sirve para que puedas ingresar textos mas largos como por ejemplo en una caja de comentarios
textoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)#Esto sirve que para cuando el comentario por defecto haga scrolling tu tienes una barra para poder moverte // scrollVert=Scrollbar(ruta, command=cajaDEtexto.yviw)la y es de vertical y viw es la funcion
scrollVert.grid(row=4, column=2, sticky="nsew")#Esto llama a la funcion y la coloca al lado // con nsew se adapta al tamano del texto

textoComentario.config(yscrollcommand=scrollVert.set)# Esto sirve paracuando textoComentario este haciendo scroll, la barra tambien lo haga en cordinacion al scroll

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)#sticky sirve para situar al norte, sur, este, oeste el texto indicado

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLable=Label(miFrame, text="Apellido:")
apellidoLable.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

def codigoBoton():

	minombre.set("Dani")#Esto sirve para cuando la variable lo llame al pulsar el boron, se escriba automaticamente en el cuadro


botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)# Comand sirve para cuando pulses el boton llames a la funcion codigoBoton
botonEnvio.pack()# Hemos creado un boton

raiz.mainloop()