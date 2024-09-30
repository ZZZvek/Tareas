from typing import List
from Materias.CL_Materia import Materia
from Grupos.CL_Grupo import Grupo
from random import randint

class Semestre:
    ID: str
    sem_numero: int
    sem_mat_carrera: str
    sem_materias: List[Materia]
    semgrupo: List[Grupo]
    
    def __init__(self, numero: int, id_carrera: str):
        self.gen_id_sem(numero)
        self.sem_mat_carrera = id_carrera
        pass
    
    def gen_id_sem(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(0,10000)-randint(0,10000)}"