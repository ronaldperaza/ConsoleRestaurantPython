import sqlite3
from tkinter import *

root = Tk()
root.title("Restaurant Liah - Menu")
root.geometry("500x710")
root.resizable(0,0)  #evitar modificar el tamaño
root.config(bd=25, relief="sunken") #border y relieve

Label(root, text="Restaurant Liah", fg="darkgreen", font=("Times New Roman", 28, "bold italic")).pack()

Label(root, text="Menu del Dia", fg="green", font=("Times New Roman", 24, "bold italic")).pack()

#Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

#Buscar las categorias y platos de bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()

for categoria in categorias:
    Label(root, text=categoria[1], fg="black", font=("Times New Roman", 20, "bold italic")).pack()

    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()

    for plato in platos:
        Label(root, text=plato[1], fg="gray", font=("Verdana", 15, "italic")).pack()

    #Separacion entre categorias
    Label(root, text="").pack()

conexion.close()

# Precio de Menu
Label(root, text="12$ (IVA incl.)", fg="darkgreen", font=(
    "Times New Roman",20,"bold italic")).pack(side="right")

#PAra ejecutar el bucle
root.mainloop()