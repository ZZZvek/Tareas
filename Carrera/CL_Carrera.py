from typing import List
from random import randint
from Materias.CL_Materia import Materia
from Estudiantes.CL_Estudiante import Estudiante
from Semestre.CL_Semestre import Semestre


class Carrera:
    ca_matricula: str
    ca_nombre: str
    ca_materia: List[Materia]
    ca_estudiante: List[Estudiante]
    ca_num_semestres: int = 0
    ca_semestres: List[Semestre] = []

    def __init__(self, nom_carrera: str):
        self.ca_matricula = self.gen_matricula(nom_carrera)
        self.ca_nombre = nom_carrera


    def gen_matricula(self, nom_carrera: str):
        return f"{nom_carrera}-{randint(0,10000)}-{randint(0,10000)}"
    
    def reg_semestre(self, semestre: Semestre):
        self.ca_num_semestres += 1
        self.ca_semestres.append(semestre)

    def mostrar_info_carrera(self):
        info = f"""Matrícula: {self.ca_matricula}
Nombre: {self.ca_nombre}
No. Semestres: {self.ca_num_semestres}"""
        return info