from tkinter import *
from tkinter import messagebox,filedialog

window=Tk()
window.title("Prueba de ventanas")
window.resizable(True,True)
window.geometry("1280x720")
window.config(bg="orange")
ruta=StringVar()

def cerrar_ventana():
    opcion=messagebox.askquestion("Adios","¿Desea cerrar la ventana?")
    if opcion=="yes":
        window.destroy()


def abrir():
    archivo=filedialog.askopenfilename(title="Ejemplo de abrir un archivo",filetypes=(("Archivos de texto","*.txt"),
    ("'Archivos python'","*py"),("Todos los ficheros","*.*")))
    ruta.set(f"{archivo}")
#Para agregar las opciones de filtrado de los tipos de archivo se deben agregar las opciones en forma de tupla detro de filetypes()


label_ruta=Label(window,text="Ruta del archivo:")
label_ruta.pack()
cuadro_ruta=Entry(window,textvariable=ruta,width="70")
cuadro_ruta.pack()
cuadro_ruta.config(bg="white",fg="green",font="Terminus",justify="center")


boton=Button(window,text="Cerrar toda la ventana",command=cerrar_ventana)
boton.pack(side="bottom")

barra_menu=Menu(window)
window.config(menu=barra_menu)

menu_file=Menu(barra_menu,tearoff=0)
menu_file.add_command(label="Open file",command=abrir)

barra_menu.add_cascade(label="File",menu=menu_file)

window.mainloop()
