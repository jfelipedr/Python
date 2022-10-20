from tkinter import Tk, Label
# rw = row | cl = column
raiz = Tk()
for rw in range(5):
    for cl in range(11):
        Label(raiz, text =' (Row %s) \n (Column = %s) ' % (rw, cl),
              borderwidth =15).grid(row = rw, column = cl)
raiz.mainloop()
