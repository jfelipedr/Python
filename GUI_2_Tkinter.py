from tkinter import *
from tkinter import messagebox
#con messagebox se pueden usa ventanas emergentes

window=Tk()
window.title("Prueba de ventanas")
window.resizable(True,True)
window.geometry("1300x700")
window.config(bg="pink",relief="sunken",bd=25)
frame=Frame()
frame.pack(side="left",anchor="n")
frame.config(bg="blue",width="400",height="250",relief="ridge",bd=10,cursor="hand2")

recordar0=Label(window,text="Recordar interactuar con: \nlos botones, \nmenus y \ncuadros de texto \ncasi todos tienen alguna funcion")
recordar0.pack(side="right",anchor="s")

nombre=Label(frame,text="Nombre:")
nombre.grid(row=0,column=0,sticky="e",padx=7,pady=7)
cuadro_nombre=Entry(frame)
cuadro_nombre.grid(row=0,column=1,padx=7,pady=7)
cuadro_nombre.config(fg="green",justify="center")

apellido=Label(frame,text="Apellido:")
apellido.grid(row=1,column=0,sticky="e",padx=7,pady=7)
cuadro_apellido=Entry(frame)
cuadro_apellido.grid(row=1,column=1,padx=7,pady=7)
cuadro_apellido.config(fg="red",justify="center")

password=Label(frame,text="Contraseña:")
password.grid(row=2,column=0,sticky="e",padx=7,pady=7)
cuadro_password=Entry(frame)
cuadro_password.grid(row=2,column=1,padx=7,pady=7)
cuadro_password.config(fg="brown",justify="center",show="*")

texto=Label(frame,text="Cuadro de texto:")
texto.grid(row=3,column=0,sticky="e",padx=7,pady=7)
cuadro_texto=Text(frame,width=30,height=10)
cuadro_texto.grid(row=3,column=1,padx=7,pady=7)

scrollV=Scrollbar(frame,command=cuadro_texto.yview)
scrollV.grid(row=3,column=2,padx=5,pady=5,sticky="nsew")
cuadro_texto.config(yscrollcommand=scrollV.set)
#este config se debe poner despues de crear el scroll, y permite elanzar la posicion del texto en el cuadro_texto
#con la posicion de la barra del scroll

def cerrar_ventana():
    opcion=messagebox.askokcancel("Adios","¿Desea cerrar la ventana version (True or False)?")
    if opcion==True:
        window.destroy()

boton=Button(frame,text="Cerrar toda la ventana",command=cerrar_ventana)
boton.grid(row=4,column=1,padx=5,pady=5)

#creacion de un menu en la ventana:
barra_menu=Menu(window)
window.config(menu=barra_menu)

#creacion de las pociones del menu desplegable file en orden de arriba hacia abajo
def opciones_de_cerrar():
    opcion_seleccionada=messagebox.askquestion("Adios","¿Desea cerrar la ventana/aplicacoin/juego/etc..?")
    if opcion_seleccionada=="yes":
        window.destroy()

menu_file=Menu(barra_menu,tearoff=0)
menu_file.add_command(label="New file")
menu_file.add_command(label="Open file")
menu_file.add_command(label="Save as")
menu_file.add_separator()
menu_file.add_command(label="Quit",command=opciones_de_cerrar)

#creacion de las pociones del menu edit file en orden de arriba hacia abajo
menu_edit=Menu(barra_menu,tearoff=0)
menu_edit.add_command(label="Undo")
menu_edit.add_command(label="Redo")
menu_edit.add_separator()
menu_edit.add_command(label="Copy")
menu_edit.add_command(label="Paste")

#creacion de las funciones al pulsar botones del menu desplegable help
def info():
    messagebox.showinfo("Info de python3 :D",
    "Para recordar como funcionan los elementos de esta ventana revisar la documentacion de: \nTkinter \nPython3")

def documentacion():
    messagebox.showwarning("0J0","Ejemplo de ventana emergente de emergencia")

menu_help=Menu(barra_menu,tearoff=0)
menu_help.add_command(label="A modo de Ejemplo",command=documentacion)
menu_help.add_command(label="Acerda de esta ventana",command=info)

#agrega los menus anteriormente creados a una barra de menu en la ventana "window"
barra_menu.add_cascade(label="File",menu=menu_file)
barra_menu.add_cascade(label="Edit",menu=menu_edit)
barra_menu.add_cascade(label="Help",menu=menu_help)

window.mainloop()
