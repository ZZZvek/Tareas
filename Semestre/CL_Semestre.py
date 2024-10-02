from typing import List
from Materias.CL_Materia import Materia
from Grupos.CL_Grupo import Grupo
from random import randint

class Semestre:
    ID: str
    sem_numero: int
    sem_mat_carrera: str
    sem_materias: List[Materia]
    sem_grupo: List[Grupo]
    
    def __init__(self, numero: int, id_carrera: str):
        self.ID = self.gen_id_sem(numero)
        self.sem_mat_carrera = id_carrera
        self.sem_numero = numero
        self.sem_materias = []
        self.sem_grupo = []
        pass

    def gen_id_sem(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(0,10000)}-{randint(0,10000)}"
    
    def reg_grupo_sem(self, grupo:Grupo):
        self.sem_grupo.append(grupo)

    def mostrar_info_semestre(self):
        info = f"""ID del semestre: {self.ID}
Número: {self.sem_numero}
Matrícula de carrera: {self.sem_mat_carrera}"""
        return info