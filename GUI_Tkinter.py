from tkinter import *

raiz=Tk()
raiz.title("Prueba de ventanas")
raiz.resizable(True,True)
#resizable por defecto tiene los dos valores en true, para poder redimendionar el ancho y alto de la ventana, se puede poner 0 como valor False
raiz.geometry("1280x720")
#geometry cambia el tamaño inicial de la ventana
raiz.config(bg="green",relief="sunken",bd=25)
#con config y bg="" se puede cambiar el color del fondo

frame=Frame()
frame2=Frame()
frame3=Frame(raiz,width="500",height="200")
#con Frame()se especifica primero donde va metido el frame(en la raiz, o en otros frames) luego el ancho y alto
frame.pack(side="right",anchor="n")
frame2.pack(side="left",anchor="s")
frame3.pack(side="left",anchor="n")
#con pack se indica que el frame va dentro de la raiz, osea la misma ventana
#pack(side="")cambia el lugar al que va anclado el frame, se puede anclar en dos coordenadas con anchor="" y usando s n w e para indicar
#norte sur este y oeste
#para mas info revisar la documentacion online
frame.config(bg="pink")
frame.config(width="450",height="350")
#se puede cambiar el ancho y alto del frame separando las propiedades con comas "," en un solo config()
frame.config(relief="groove",bd=15)
#con relief se asigna el tipo de borde y con bd se asigna el grosor del borde medido px
frame.config(cursor="hand2")
#cursor cambia el tipo del cursor al pasar el mouse sobre ese frame
frame2.config(bg="purple",width="400",height="250",relief="ridge",bd=30,cursor="pirate")
frame3.config(bg="white",relief="solid",bd=10)
label=Label(frame3,text="Texto de prueba dentro del frame 3",fg="blue")
label.place(x=0,y=0)
#con place indica cuanto debe correr el texto desde el borde izquierdo y superior del frame respectivamente
Label(raiz,text="Lo de arriba es un cuadro de texto editable",fg="red",font="Terminus").place(x=450,y=400)
#se pued reducir espacio en el codigo en caso de que la variable del label no se vaya a usar por el programa.
cuadro_texto=Entry(raiz)
#con Entry se crea un cuadro de texto editable
cuadro_texto.place(x=500,y=370)

raiz.mainloop()
#mainloop siempre va de ultimo y permite manterner la ventana
