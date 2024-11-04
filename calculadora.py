import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

def sumar():
    try:
        num1 = float(ent_n1.get())
        num2 = float(ent_n2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def restar():
    try:
        num1 = float(ent_n1.get())
        num2 = float(ent_n2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def multiplicar():
    try:
        num1 = float(ent_n1.get())
        num2 = float(ent_n2.get())
        multiplcacion = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicación es: {multiplcacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def dividir():
    try:
        num1 = float(ent_n1.get())
        num2 = float(ent_n2.get())
        division = num1 / num2
        messagebox.showinfo("Resultado", f"La división es: {division}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "¿Si fuiste al kinder o no?")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")



lab_n1 = tk.Label(ventana,text="1er número")
lab_n1.pack(pady=10)
ent_n1 = tk.Entry(ventana)
ent_n1.pack(pady=10)

lab_n2 = tk.Label(ventana,text="2do número")
lab_n2.pack(pady=10)
ent_n2 = tk.Entry(ventana)
ent_n2.pack(pady=10)

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=20)

boton_sumar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_sumar.pack(pady=20)

boton_sumar = tk.Button(ventana, text="Restar", command=restar)
boton_sumar.pack(pady=20)

boton_sumar = tk.Button(ventana, text="Dividir", command=dividir)
boton_sumar.pack(pady=20)

ventana.mainloop()