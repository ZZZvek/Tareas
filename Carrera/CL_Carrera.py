from typing import List
from Materias.CL_Materia import Materia
from Estudiantes.CL_Estudiante import Estudiante
from Semestre.CL_Semestre import Semestre


class Carrera:
    ca_matricula: str
    ca_nombre: str
    ca_materia: List[Materia]
    ca_estudiante: List[Estudiante]
    ca_num_semestres: int
    ca_semestres: List[Semestre]