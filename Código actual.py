import tkinter as tk
from PIL import ImageTk, Image
#definicion
def graf_1():
    ventana = tk.Toplevel()
    ventana.title("Gráfica de barras")
    ventana.geometry("300x400")
    ventana.configure(bg="#5a6879")
    
    etiqueta = tk.Label(ventana, text="Aca debe haber un grafico")
    etiqueta.pack()
#ventana principal
root = tk.Tk()
root.title("Notas Smart")
#textos
saludo = tk.Label(
    root,
    text="¡Hola profesor!",
    font=("Arial", 10, "bold"),
    relief="raised",
    bd=4
    )
#boton
vent_1 = tk.Button(
    root, 
    text="Gráfica de barras",
    command=graf_1,
    padx=20,
    pady=10
    )
#imagen
prin = Image.open("Documents\Proyectos Python\logo-usach.png")
prin = prin.resize((150, 53))
prin_tk = ImageTk.PhotoImage(prin)
et_prin = tk.Label(root, image=prin_tk)
###
et_prin.pack(pady=30)
saludo.pack(pady=32)
vent_1.pack(padx=10, pady=35)
root.geometry("600x700")
root.mainloop()
