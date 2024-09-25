from typing import List
from Estudiantes.CL_Estudiante import Estudiante
from Maestros.CL_Maestro import Maestro
from Materias.CL_Materia import Materia

class Grupo:
    ID: int
    gr_alumnos: List[Estudiante] = []
    gr_maestro: List[Maestro] = []
    gr_materias: List[Materia] = []
    tipo: chr