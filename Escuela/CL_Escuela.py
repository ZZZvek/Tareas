from typing import List
from datetime import datetime
from random import randint
from Estudiantes.CL_Estudiante import Estudiante
from Grupos.CL_Grupo import Grupo
from Maestros.CL_Maestro import Maestro
from Materias.CL_Materia import Materia

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_grupos: List[Grupo] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    
    def reg_estudiante(self, estudianteReg: Estudiante):
        self.lista_estudiantes.append(estudianteReg)
        
    def reg_maestro(self, maestroReg: Maestro):
        self.lista_maestros.append(maestroReg)
        
    def gen_num_control_estudiante(self):
        num_control_estudiante = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0,10000)}"
        return num_control_estudiante
    
    def gen_num_control_maestro(self, maestro: Maestro):
        ano_nacimiento = maestro.ma_ano_nacimiento
        letras_nombre = maestro.ma_nombre[:2].upper()
        letras_rfc = maestro.ma_rfc[:-2].upper()
        longitud = len(self.lista_maestros) + 1
        num_control_maestro = f"L{ano_nacimiento}{datetime.now().day}{datetime.now().year}{randint(500,5000)}{letras_nombre}{letras_rfc}{longitud}"
        
        return num_control_maestro
        