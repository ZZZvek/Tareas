import tkinter as tk
import mysql.connector
from tkinter import ttk, messagebox
from tkinter import *

def mostrar():
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
    cursor = mysqlC.cursor()
    cursor.execute("select * from usuarios")
    lista = cursor.fetchall()
    
    for i, (identificador, nombre, apellido, usuario, contraseña, rol) in enumerate(lista, start=1):
        listbox.insert("", "end", values=(identificador, nombre, apellido, usuario, contraseña, rol))
    mysqlC.close()

def añadir():
    nombre_Add = nombre.get()
    apellido_Add = apellido.get()
    usuario_Add = usuario.get()
    contraseña_Add = contraseña.get()
    rol_Add = rol.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
    cursor = mysqlC.cursor()
    
    try:
        cursor.execute(
            f"INSERT INTO usuarios(nombre, apellido, usuario, contraseña, rol) VALUES('{nombre_Add}', '{apellido_Add}', '{usuario_Add}', '{contraseña_Add}', '{rol_Add}')"
        )
        mysqlC.commit()
        limpiar_campos()
        messagebox.showinfo("Información", "Usuario agregado.")
        refresh()

    except Exception as e:
        print(e)
        mysqlC.rollback()

    finally:
        mysqlC.close()

def borrar():
    user_delete = usuario.get()
    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
    cursor = mysqlC.cursor()
    
    try:
        cursor.execute("DELETE FROM usuarios WHERE usuario=%s", (user_delete,))
        mysqlC.commit()
        limpiar_campos()
        messagebox.showinfo("Información", "Usuario eliminado.")
        refresh()

    except Exception as e:
        print(e)
        mysqlC.rollback()

    finally:
        mysqlC.close()

def obtenerR(event):
    limpiar_campos()
    renglon = listbox.selection()[0]
    seleccion = listbox.set(renglon)
    nombre.insert(0, seleccion["Nombre"])
    apellido.insert(0, seleccion["Apellidos"])
    usuario.insert(0, seleccion["Usuario"])
    contraseña.insert(0, seleccion["Contraseña"])
    rol.insert(0, seleccion["Rol"])

def refresh():
    for i in listbox.get_children():
        listbox.delete(i)
    mostrar()

def editar():
    nombre_Add = nombre.get()
    apellido_Add = apellido.get()
    usuario_Add = usuario.get()
    contraseña_Add = contraseña.get()
    rol_Add = rol.get()
    selected_item = listbox.selection()
    if not selected_item:
        messagebox.showerror("Error", "Por favor selecciona un registro para editar.")
        return
    renglon = listbox.set(selected_item[0])
    id_usuario = renglon["ID"]

    mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
    cursor = mysqlC.cursor()

    try:
        cursor.execute(
            "UPDATE usuarios SET nombre=%s, apellido=%s, usuario=%s, contraseña=%s, rol=%s WHERE id=%s",
            (nombre_Add, apellido_Add, usuario_Add, contraseña_Add, rol_Add, id_usuario)
        )
        mysqlC.commit()
        limpiar_campos()
        messagebox.showinfo("Información", "Usuario editado correctamente.")
        refresh()

    except mysql.connector.Error as e:
        print(e)
        messagebox.showerror("Error", "Ocurrió un problema al editar el usuario.")
        mysqlC.rollback()

    finally:
        mysqlC.close()

def limpiar_campos():
    nombre.delete(0, END)
    apellido.delete(0, END)
    usuario.delete(0, END)
    contraseña.delete(0, END)
    rol.delete(0, END)

root = tk.Tk()
root.geometry("1200x800")
root.title("Gestión de Usuarios")
root.config(bg="#f0f0f0")

tk.Label(root, text="Gestión de Usuarios", font=("Helvetica", 28, "bold"), fg="#333", bg="#f0f0f0").pack(pady=20)

form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

labels = ["Nombre", "Apellido", "Usuario", "Contraseña", "Rol"]
entries = []

for i, text in enumerate(labels):
    tk.Label(form_frame, text=text, font=("Helvetica", 12), bg="#f0f0f0").grid(row=i, column=0, padx=20, pady=10, sticky="e")
    entry = tk.Entry(form_frame, font=("Helvetica", 12), width=25, relief="solid", bd=1)
    entry.grid(row=i, column=1, pady=10, sticky="w")
    entries.append(entry)

nombre, apellido, usuario, contraseña, rol = entries

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

button_config = {"font": ("Helvetica", 12, "bold"), "width": 12, "height": 2}

tk.Button(button_frame, text="Crear", bg="#4caf50", fg="white", command=añadir, **button_config).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Editar", bg="#2196f3", fg="white", command=editar, **button_config).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Eliminar", bg="#f44336", fg="white", command=borrar, **button_config).grid(row=0, column=2, padx=10)

columnas = ("ID", "Nombre", "Apellidos", "Usuario", "Contraseña", "Rol")
listbox = ttk.Treeview(root, columns=columnas, show="headings", height=15)
listbox.pack(pady=20)

for col in columnas:
    listbox.heading(col, text=col)
    listbox.column(col, width=180, anchor="center")

mostrar()
listbox.bind("<Double-Button-1>", obtenerR)

root.mainloop()