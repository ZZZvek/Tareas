class Materia:
    num_c_materia: str
    mt_nombre: str
    descripcion: str
    semestre: int
    creditos: int
    
    def __init__(self, num_materia:str, nombre:str, descripcion:str, semestre:int, creditos:int):
        self.num_c_materia = num_materia
        self.mt_nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos