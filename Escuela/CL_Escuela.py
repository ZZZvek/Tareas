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
        
    def reg_materia(self, materiaReg:Materia):
        self.lista_materias.append(materiaReg)
        
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
    
    def gen_num_control_materia(self, materia:Materia):
        letras_nombre = materia.mt_nombre[:-2].upper()
        semestre = materia.semestre
        creditos = materia.creditos
        random = randint(1,1000)
        
        num_c_materia = f"MT{letras_nombre}{semestre}{creditos}{creditos}{random}"
        
        return num_c_materia
    
    def listar_estudiantes(self):
        print("-----ESTUDIANTES-----")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
            return
            
    def listar_maestros(self):
        print("-----MAESTROS-----")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
            return
    
    def listar_materias(self):
        print("-----MATERIAS-----")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
            return
            
    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.es_numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                return
        print("---No se encontró el estudiante---")

    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.ma_numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                return
        print("---No se encontró al maestro---")

    def eliminar_materia(self, numero_control: str):
        for materia in self.lista_materias:
            if materia.num_c_materia == numero_control:
                self.lista_materias.remove(materia)
                return
        print("---No se encontró la materia---")