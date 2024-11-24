import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from tkinter import *

def limpiar_login():
    entry_usuario.delete(0, END)
    entry_contraseña.delete(0, END)
    
def verificar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
 
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='proyecto'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s
        ''', (usuario, contraseña))
 
        usuario = cursor.fetchone()

        if usuario:
            rol = usuario[5].lower()
            if rol== "administrador":
                messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
                limpiar_login()
                abrir_admin_ventana()
                
            elif rol=="usuario":
                messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[1]}")
                limpiar_login()
                abrir_usuario_ventana()
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
  
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()  



def abrir_admin_ventana():

    def mostrar_usuarios():
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
        cursor = mysqlC.cursor()
        cursor.execute("select * from usuarios")
        lista = cursor.fetchall()
    
        for i, (identificador, nombre, apellido, usuario, contraseña, rol) in enumerate(lista, start=1):
            listbox.insert("", "end", values=(identificador, nombre, apellido, usuario, contraseña, rol))
        mysqlC.close()

    def añadir_usuarios():
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
            limpiar_campos_usuarios()
            messagebox.showinfo("Información", "Usuario agregado.")
            refresh()

        except Exception as e:
            print(e)
            mysqlC.rollback()

        finally:
            mysqlC.close()

    def borrar_usuarios():
        user_delete = usuario.get()
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
        cursor = mysqlC.cursor()
    
        try:
            cursor.execute("DELETE FROM usuarios WHERE usuario=%s", (user_delete,))
            mysqlC.commit()
            limpiar_campos_usuarios()
            messagebox.showinfo("Información", "Usuario eliminado.")
            refresh()

        except Exception as e:
            print(e)
            mysqlC.rollback()

        finally:
            mysqlC.close()

    def obtenerR_usuarios(event):
        limpiar_campos_usuarios()
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
        mostrar_usuarios()

    def editar_usuarios():
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
            limpiar_campos_usuarios()
            messagebox.showinfo("Información", "Usuario editado correctamente.")
            refresh()

        except mysql.connector.Error as e:
            print(e)
            messagebox.showerror("Error", "Ocurrió un problema al editar el usuario.")
            mysqlC.rollback()

        finally:
            mysqlC.close()

    def limpiar_campos_usuarios():
        nombre.delete(0, END)
        apellido.delete(0, END)
        usuario.delete(0, END)
        contraseña.delete(0, END)
        rol.delete(0, END)

    def regresar_a_login():
        root_usuario.destroy()  
        root.deiconify()

    root.withdraw()
    root_usuario = tk.Toplevel(root)
    root_usuario.geometry("1200x800")
    root_usuario.title("Gestión de Usuarios")
    root_usuario.config(bg="#f0f0f0")

    tk.Label(root_usuario, text="Gestión de Usuarios", font=("Oswald",28,), fg="black", bg="#f0f0f0").pack(pady=20)

    form_frame = tk.Frame(root_usuario, bg="#f0f0f0")
    form_frame.pack(pady=10)

    labels = ["Nombre", "Apellido", "Usuario", "Contraseña", "Rol"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(form_frame, text=text, font=("Helvetica", 12), bg="#f0f0f0").grid(row=i, column=0, padx=20, pady=10, sticky="e")
        entry = tk.Entry(form_frame, font=("Helvetica", 12), width=25, relief="solid", bd=1)
        entry.grid(row=i, column=1, pady=10, sticky="w")
        entries.append(entry)

    nombre, apellido, usuario, contraseña, rol = entries

    button_frame = tk.Frame(root_usuario, bg="#f0f0f0")
    button_frame.pack(pady=20)

    button_config = {"font": ("Helvetica", 12, "bold"), "width": 12, "height": 2}

    tk.Button(button_frame, text="Crear", bg="gray", fg="white", command=añadir_usuarios, **button_config).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Editar", bg="gray", fg="white", command=editar_usuarios, **button_config).grid(row=0, column=1, padx=10)
    tk.Button(button_frame, text="Eliminar", bg="gray", fg="white", command=borrar_usuarios, **button_config).grid(row=0, column=2, padx=10)
    tk.Button(button_frame, text="Salir", bg="gray", fg="white", command=regresar_a_login, **button_config).grid(row=0, column=3, padx=10)

    columnas = ("ID", "Nombre", "Apellidos", "Usuario", "Contraseña", "Rol")
    listbox = ttk.Treeview(root_usuario, columns=columnas, show="headings", height=15)
    listbox.pack(pady=20)

    for col in columnas:
        listbox.heading(col, text=col)
        listbox.column(col, width=180, anchor="center")

    mostrar_usuarios()
    listbox.bind("<Double-Button-1>", obtenerR_usuarios)

    root_usuario.mainloop()  

def abrir_usuario_ventana():
    def mostrar_libros():
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
        micursos = mysqlC.cursor()
        micursos.execute("select * from libros")
        lista = micursos.fetchall()

        for i in listbox.get_children():
                listbox.delete(i)

        for i,(id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
            listbox.insert("", "end", values=(id, titulo, autor, editorial, año_publicacion, precio))
        mysqlC.close()

    def actualizar_libros():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar_libros()

    def add_libros():
        tituloAdd = titulo.get()
        autorAdd = autor.get()
        editorialAdd = editorial.get()
        año_publicacionAdd = año_publicacion.get()
        precioAdd = precio.get()
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"insert into libros(titulo, autor, editorial, año_publicacion, precio) values('{tituloAdd}','{autorAdd}','{editorialAdd}','{año_publicacionAdd}','{precioAdd}')")
            mysqlC.commit()
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año_publicacion.delete(0,END)
            precio.delete(0,END)
            messagebox.showinfo("informacion", "libro agregado")
            actualizar_libros()

        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def delete_libros():
        seleccion = listbox.selection() 
        if seleccion:
            identificador = listbox.item(seleccion[0], "values")[0]

        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"DELETE FROM LIBROS WHERE id={identificador}")
            mysqlC.commit()
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año_publicacion.delete(0,END)
            precio.delete(0,END)
            messagebox.showinfo("informacion", "libro eliminado")
            actualizar_libros()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit_libros():
        seleccion = listbox.selection()
        if seleccion:
            identificador = listbox.item(seleccion[0], "values")[0]

        tituloAdd = titulo.get()
        autorAdd = autor.get()
        editorialAdd = editorial.get()
        año_publicacionAdd = año_publicacion.get()
        precioAdd = precio.get()
        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database= "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"UPDATE libros set titulo='{tituloAdd}', autor='{autorAdd}', editorial ='{editorialAdd}', año_publicacion='{año_publicacionAdd}', precio='{precioAdd}' where id={identificador}")
            mysqlC.commit()
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año_publicacion.delete(0,END)
            precio.delete(0,END)
            messagebox.showinfo("informacion", "libro editado")
            actualizar_libros()

        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def filtrar_por_editorial():
        editorial_filtro = editorial_f.get()
        if not editorial_filtro:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una editorial para filtrar.")
            return

        mysqlC = mysql.connector.connect(host="localhost", user="root", password="", database="proyecto")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"SELECT * FROM libros WHERE editorial = %s", (editorial_filtro,))
            lista = micursos.fetchall()
        
            for i in listbox.get_children():
                listbox.delete(i)

            for i, (id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
                listbox.insert("", "end", values=(id, titulo, autor, editorial, año_publicacion, precio))

            if not lista:
                messagebox.showinfo("Información", f"No se encontraron libros de la editorial '{editorial_filtro}'.")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Ocurrió un error al filtrar.")
            mysqlC.close()

    def obtenerR_libros(event):
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        año_publicacion.delete(0,END)
        precio.delete(0,END)
    
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        titulo.insert(0, seleccion["Titulo"])
        autor.insert(0, seleccion["Autor"])
        editorial.insert(0, seleccion["Editorial"])
        año_publicacion.insert(0, seleccion["Año de publicacion"])
        precio.insert(0, seleccion["Precio"])   

    def regresar_a_login():
        root_libros.destroy()  
        root.deiconify()  

    
    root.withdraw()
    root_libros = tk.Tk()
    root_libros.geometry("1200x600")
    root_libros.title("Usuario")
    
    label1 = tk.Label(root_libros,text="REGISTRO DE LIBROS", fg="purple",font=("Broadway",28)).place(x=400,y=0)
    
    global titulo
    global autor
    global editorial
    global año_publicacion
    global precio

    labeltitulo = tk.Label(root_libros, text="Titulo", font=("Georgia", 13))
    labeltitulo.place(x=100, y=80)
    
    labelautor = tk.Label(root_libros, text="Autor", font=("Georgia", 13))
    labelautor.place(x=100, y=110)
    
    labeleditorial = tk.Label(root_libros, text="Editorial", font=("Georgia", 13))
    labeleditorial.place(x=100, y=140)
    
    labelaño_publicacion = tk.Label(root_libros, text="Año de Publicacion", font=("Georgia", 13))
    labelaño_publicacion.place(x=650, y=80)

    labelprecio = tk.Label(root_libros, text="Precio", font=("Georgia", 13))
    labelprecio.place(x=650, y=110)

    label_filtro = tk.Label(root_libros, text="Filtrar por Editorial", font=("Georgia", 13))
    label_filtro.place(x=650, y=140)
    
    titulo = tk.Entry(root_libros)
    titulo.place(x=270, y=80)
    
    autor = tk.Entry(root_libros)
    autor.place(x=270, y=110)
    
    editorial = tk.Entry(root_libros)
    editorial.place(x=270, y=140)

    año_publicacion = tk.Entry(root_libros)
    año_publicacion.place(x=820, y=80)

    precio = tk.Entry(root_libros)
    precio.place(x=820, y=110)

    editorial_f = tk.Entry(root_libros)
    editorial_f.place(x=820, y=140)

    tk.Button(root_libros,text="Crear", command=add_libros, height=5, width=10, font=("Rockwell",14)).place(x=350,y=250)
    tk.Button(root_libros,text="Editar",command=edit_libros, height=5, width=10, font=("Rockwell",14)).place(x=500,y=250)
    tk.Button(root_libros,text="Eliminar",command=delete_libros, height=5, width=10, font=("Rockwell",14)).place(x=650,y=250)
    tk.Button(root_libros, text="Salir", command=regresar_a_login, height=1, width=12, font=("Rockwell", 14)).place(x=950, y=250)
    tk.Button(root_libros, text="Filtrar", command=filtrar_por_editorial, height=1, width=10, font=("Rockwell", 14)).place(x=820, y=170)
    tk.Button(root_libros, text="Mostrar todo", command=mostrar_libros, height=1, width=12, font=("Rockwell", 14)).place(x=950, y=170)

    
    columnas = ("Id","Titulo","Autor","Editorial", "Año de publicacion", "Precio")
    listbox = ttk.Treeview(root_libros,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=400)
 
    mostrar_libros()
    listbox.bind("<Double-Button-1>",obtenerR_libros)

    root_libros.mainloop()
    
    def regresar_a_login():
        root_libros.destroy()  
        root.deiconify()
    


root= tk.Tk()
root.title("Login")
root.geometry("300x200") 

label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root, width=30)
entry_usuario.pack(pady=5)
 
label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(root, width=30, show="*")
entry_contraseña.pack(pady=5)


btn_login = tk.Button(root, text="Login", command=verificar_usuario)
btn_login.pack(pady=20)
 
root.mainloop()