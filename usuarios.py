import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *
     
def mostrar():
    mysqlC = mysql.connector.connect(host="localhost", user="root", password= "", database="proyecto")
    cursor = mysqlC.cursor()
    cursor.execute("select * from usuarios")
    lista = cursor.fetchall()
    
    for i, (identificador, nombre, apellido, usuario, contraseña, rol) in enumerate(lista,start=1):
        listbox.insert("","end",values=(identificador, nombre, apellido, usuario, contraseña, rol))
        mysqlC.close()
        
def añadir():
    nombre_Add = nombre.get()
    apellido_Add = apellido.get()
    usuario_Add = usuario.get()
    contraseña_Add = contraseña.get()
    rol_Add = rol.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password= "", database="proyecto")
    cursor = mysqlC.cursor()
    
    try:
        
        cursor.execute(f"insert into usuarios(nombre, apellido, usuario, contraseña, rol) values('{nombre_Add}', '{apellido_Add}', '{usuario_Add}', '{contraseña_Add}', '{rol_Add}')")
        mysqlC.commit()
        nombre.delete(0, END)
        apellido.delete(0, END)
        usuario.delete(0, END)
        contraseña.delete(0, END)
        rol.delete(0, END)
        messagebox.showinfo("Información","Usuario agregado.")
        refresh()
        
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()
        
def borrar():
    user_delete = usuario.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
    cursor = mysqlC.cursor()
    
    try:
        cursor.execute("DELETE FROM usuarios WHERE usuario=%s", (user_delete,))
        mysqlC.commit()

        nombre.delete(0, END)
        apellido.delete(0, END)
        usuario.delete(0, END)
        contraseña.delete(0, END)
        rol.delete(0, END)
        messagebox.showinfo("Información", "Usuario eliminado.")
        refresh()

    except Exception as e:
        print(e)
        mysqlC.rollback()
        
def editar():
    nombre_Add = nombre.get()
    apellido_Add = apellido.get()
    usuario_Add = usuario.get()
    contraseña_Add = contraseña.get()
    rol_Add = rol.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password= "", database="proyecto")
    cursor = mysqlC.cursor()
    
    try:
        
        cursor.execute(f"UPDATE usuarios set nombre = '{nombre_Add}', apellido = '{apellido_Add}', usuario = '{usuario_Add}', contraseña = '{contraseña_Add}', rol = '{rol_Add}' where usuario = '{usuario_Add}'")
        mysqlC.commit()
        nombre.delete(0,END)
        apellido.delete(0,END)
        usuario.delete(0,END)
        contraseña.delete(0,END)
        rol.delete(0, END)
        messagebox.showinfo("Información","Usuario editado.")
        refresh()
        
    except Exception as e:
        print(e)
        mysqlC.rollback()
        mysqlC.close()
        
def refresh():
    for i in listbox.get_children():
        listbox.delete(i)
    mostrar()
        
def obtenerR(event):
    nombre.delete(0,END)
    apellido.delete(0,END)
    usuario.delete(0,END)
    contraseña.delete(0,END)
    rol.delete(0, END)
    
    renglon = listbox.selection()[0]
    print(renglon)
    seleccion = listbox.set(renglon)
    print(seleccion)
    nombre.insert(0,seleccion["Nombre"])
    apellido.insert(0,seleccion["Apellidos"])
    usuario.insert(0,seleccion["Usuario"])
    contraseña.insert(0,seleccion["Contraseña"])
    rol.insert(0,seleccion["Rol"])
        
#----------------------------------------------------------------------Botones y entradas de registro-----------------------------------------------------------

root = tk.Tk()
root.geometry("1920x1080")
 
label1 = tk.Label(root,text="Registro de usuarios", fg="red",font=("Arial",28)).place(x=170,y=0)
 
global nombre
global apellido
global usuario
global contraseña
global rol
 
labelnombre = tk.Label(root, text="Nombre", font=("Arial", 12))
labelnombre.place(x=100, y=50)
 
labelapellido = tk.Label(root, text="Apellido", font=("Arial", 12))
labelapellido.place(x=100, y=80)
 
labelusuario = tk.Label(root, text="Usuario", font=("Arial", 12))
labelusuario.place(x=100, y=110)
 
labelcontraseña = tk.Label(root, text="Contraseña", font=("Arial", 12))
labelcontraseña.place(x=100, y=140)

labelrol = tk.Label(root, text="Rol", font=("Arial", 12))
labelrol.place(x=100, y=170)
 
nombre = tk.Entry(root)
nombre.place(x=270, y=50)

apellido = tk.Entry(root)
apellido.place(x=270, y=80)
 
usuario = tk.Entry(root)
usuario.place(x=270, y=110)
 
contraseña = tk.Entry(root)
contraseña.place(x=270, y=140)

rol = tk.Entry(root)
rol.place(x=270, y=170)
 
tk.Button(root,text="Crear",command=añadir, height=5, width=10, font=("Arial",12)).place(x=100,y=200)
tk.Button(root,text="Editar",command=editar, height=5, width=10, font=("Arial",12)).place(x=250,y=200)
tk.Button(root,text="Eliminar",command=borrar, height=5, width=10, font=("Arial",12)).place(x=400,y=200)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
 
columnas = ("ID", "Nombre","Apellidos","Usuario","Contraseña", "Rol")
listbox = ttk.Treeview(root,columns=columnas,show="headings")
 
for col in columnas:
    listbox.heading(col, text=col)
    listbox.grid(row=1, column=0, columnspan=1)
    listbox.place(x=0, y=300)
 
mostrar()
listbox.bind("<Double-Button-1>", obtenerR)
 
 
root.mainloop()