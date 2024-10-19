from typing import List
from random import randint
from Estudiantes.CL_Estudiante import Estudiante
from Materias.CL_Materia import Materia

class Grupo:
    ID: str
    gr_alumnos: List[Estudiante] = []
    gr_materias: List[Materia] = []
    gr_id_semestre: str
    tipo: chr

    def __init__(self, tipo: chr, id_semestre: str):
        self.ID = self.gen_id_grupo(tipo)
        self.tipo = tipo
        self.gr_id_semestre = id_semestre
        pass

    def gen_id_grupo(self, tipo: chr) -> str:
        return f"{tipo}-{randint(0,10000)}-{randint(0,10000)}"
    
    def mostrar_info_grupo(self):
        info = f"""ID del grupo: {self.ID}
Tipo: {self.tipo}
ID del Semestre: {self.gr_id_semestre}"""
        return info
    
    def reg_estudiante(self, estudiante: Estudiante):
        self.gr_alumnos.append(estudiante)
        
    def reg_materia(self, materia: Materia):
        self.gr_materias.append(materia)
        
    def mostrar_info_grupo_estudiante(self):
        print(f"""Información del grupo:
Tipo: {self.tipo}
Semestre: {self.gr_id_semestre}""")
        
        for materia in self.gr_materias:
            print(materia.mostrar_info_materia())
        
        pass