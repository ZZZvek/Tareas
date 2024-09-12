class circulo:
    radio = 0
    
    #Constructor
    def __init__(self, radio):
        self.radio = radio
        
    #Perímetro
    def calcular_perimetro(self):

        perimetro = (2) * (3.1416) * (self.radio)
        print("El perimetro es: ", perimetro)
        print("El radio es: ", self.radio)        
    #Área
    def calcular_area(self):
        area = (3.1416) * (self.radio) * (self.radio)
        print("El área es :", area)