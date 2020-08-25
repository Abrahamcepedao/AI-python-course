from tkinter import*

windows = Tk()
windows.title("Despejador")
windows.geometry("500x500")

txt = Entry(windows, width = 20)
txt.grid(column = 0, row = 0)
lbl = Label(windows, text = "Resultado", font = ("Arial Bold", 20))
lbl.grid(column = 0, row = 1)

def clicked():
    resultado = ""
    funcion = txt.get()
    funciones = funcion.split("=")
    funcion_izq = funciones[0]
    if "+" in funcion_izq:
        funciones_simples = funcion_izq.split("+")
        if "-" not in funciones_simples[1]:
            #resultado = funciones_simples[0] + "=" + "-" + funciones_simples[1]
            valorDer = "-" + funciones_simples[1]
            valoresPar = funciones_simples[0].split("(")[0]
            variable = funciones_simples[0].split("(")[1].split(")")[0]
            resultado = variable + "=" + "(" + valorDer + ")" + "/" + valoresPar

            pass
        elif "+" not in funciones_simples[0]:
            pass
    elif "-" in funcion_izq:
        funciones_simples = funcion_izq.split("-")    
    lbl.config(text = resultado)

btn = Button(windows, text = "calcular", command = clicked)
btn.grid(column = 1, row = 0)




windows.mainloop()
















