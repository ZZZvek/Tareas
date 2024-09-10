import datetime
class Coche:
    marca= ""
    modelo = ""
    año = 0
    
    #Método constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    #Método mostrar_info
    def mostrar_info(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)
        
    #Método antigüedad
    def edad_auto(self):
        año_actual = datetime.datetime.now().year
        antiguedad = año_actual - self.año
        return antiguedad
    