class Maestro:
    ma_numero_control: str
    ma_nombre: str
    ma_ano_nacimiento: int
    ma_apellido: str
    ma_sueldo: float
    ma_rfc: str
    
    #Método constructor
    #Siempre que estamos dentro de una clase usamos self
    def __init__(self, numero_control: str, nombre: str, apellido: str, sueldo: float, rfc: str, ano_nacimiento: str):
        self.ma_numero_control: numero_control
        self.ma_nombre = nombre
        self.ma_ano_nacimiento = ano_nacimiento
        self.ma_apellido = apellido
        self.ma_sueldo = sueldo
        self.ma_rfc = rfc