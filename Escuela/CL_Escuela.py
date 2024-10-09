from typing import List
from datetime import datetime
from random import randint
from Estudiantes.CL_Estudiante import Estudiante
from Grupos.CL_Grupo import Grupo
from Maestros.CL_Maestro import Maestro
from Materias.CL_Materia import Materia
from Carrera.CL_Carrera import Carrera
from Semestre.CL_Semestre import Semestre
from Usuario.CL_Usuario import Usuario
from Coordinador.CL_Coordinador import Coordinador

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_grupos: List[Grupo] = []
    lista_maestros: List[Maestro] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    lista_usuario: List[Usuario] = []
    
    def __init__(self):
        coordinador = Coordinador(
            co_numero_control= "123",
            co_nombre= "Nico",
            co_apellido= "Ponciano",
            co_contraseña= "123",
            co_sueldo= 1000,
            co_rfc= "QWERTY",
            co_antiguedad= 15   
        )
        self.lista_usuario.append(coordinador)

        estudiante = Estudiante(
            numero_control="456",
            nombre="Kevin",
            apellido="García",
            curp="GAHK",
            f_nacimiento=datetime(2003,12,20),
            contraseña="456"
        )
        self.lista_usuario.append(estudiante)

        maestro = Maestro(
            ma_numero_control="789",
            ma_nombre="Oscar",
            ma_apellido="Coronado",
            sueldo=3000,
            rfc="OSCGOS",
            ano_nacimiento="1990",
            contraseña="789"
        )
        self.lista_usuario.append(maestro)

    def reg_estudiante(self, estudianteReg: Estudiante):
        self.lista_usuario.append(estudianteReg)
        self.lista_estudiantes.append(estudianteReg)
        
    def reg_maestro(self, maestroReg: Maestro):
        self.lista_usuario.append(maestroReg)
        self.lista_maestros.append(maestroReg)
        
    def reg_materia(self, materiaReg:Materia):
        self.lista_materias.append(materiaReg)

    def reg_carrera(self, carreraReg:Carrera):
        self.lista_carreras.append(carreraReg)
        
    def reg_semestre(self, semestreReg:Semestre):
        id_carrera = semestreReg.sem_mat_carrera
        for Carrera in self.lista_carreras:
            if Carrera.ca_matricula == id_carrera:
                Carrera.reg_semestre(semestre=semestreReg)
                break

        self.lista_semestres.append(semestreReg)

    def reg_grupo(self, grupoReg:Grupo):
        id_semestre = grupoReg.gr_id_semestre

        for Semestre in self.lista_semestres:
            if id_semestre == Semestre.ID:
                Semestre.reg_grupo_sem(grupo=grupoReg)
                break

        self.lista_grupos.append(grupoReg)

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
    
    def listar_carreras(self):
        print("-----CARRERAS-----")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
            return
        
    def listar_semestres(self):
        print("-----SEMESTRES-----")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())
            return
        
    def listar_grupos(self):
        print("-----GRUPOS-----")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
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
        
    def validar_inicio_sesion(self, num_control: str, contraseña: str):
        for usuario in self.lista_usuario:
            if usuario.numero_control == num_control:
                if usuario.contraseña == contraseña:
                    return usuario
        return None