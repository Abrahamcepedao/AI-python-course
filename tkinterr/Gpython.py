from tkinter import *

windows = Tk()
windows.title("Curso de python")
windows.geometry('800x800')
estado = True
lbl = Label(windows, text = "hello", font=("Avenir Bold", 50))
lbl.grid(column = 0, row = 0)
txt = Entry(windows, width = 10)
txt.grid(column = 1, row = 0)

def decorador(func):
    def inner(data):
        if "luis" in data:
            data = "You do not have acces"
            return
        return func(data)    
    return inner

@decorador
def imprimir(data):
   lbl.configure(text = "hola " + data)

def clicked():
    data = txt.get()
    imprimir(data)
    """
    global estado
    if estado:
        lbl.configure(text = "click")
    else:
        lbl.configure(text = "hello")
    estado = not estado    
    """


btn = Button(windows, text = "click", command = clicked)
btn.grid(column = 2, row = 0)
windows.mainloop()













