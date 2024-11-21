class Error(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        
        
def escribir_nombre(nombre):
    if (nombre == ""):
        raise Error("Se deben llenar todas las casillas.")
    
    else:
        print(f"El nombre es: {nombre}")
        
try:
    saludo = escribir_nombre("")
    print (saludo)
except Error as e:
    print(e)