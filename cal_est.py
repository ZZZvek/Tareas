import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x350")
ventana.configure(bg="gray15")

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

lab_n1 = tk.Label(ventana, text="1er número", bg="gray15", fg="white", font=("Helvetica", 12, "bold"))
lab_n1.pack(pady=5)
ent_n1 = tk.Entry(ventana, font=("Helvetica", 12), bd=2, relief="solid")
ent_n1.pack(pady=5)

lab_n2 = tk.Label(ventana, text="2do número", bg="gray15", fg="white", font=("Helvetica", 12, "bold"))
lab_n2.pack(pady=5)
ent_n2 = tk.Entry(ventana, font=("Helvetica", 12), bd=2, relief="solid")
ent_n2.pack(pady=5)

boton_sumar = tk.Button(ventana, text="Sumar", bg="dimgray", fg="white", font=("Helvetica", 10, "bold"), command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", bg="darkslategray", fg="white", font=("Helvetica", 10, "bold"), command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", bg="darkolivegreen", fg="white", font=("Helvetica", 10, "bold"), command=multiplicar)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="Dividir", bg="darkred", fg="white", font=("Helvetica", 10, "bold"), command=dividir)
boton_dividir.pack(pady=5)

ventana.mainloop()
