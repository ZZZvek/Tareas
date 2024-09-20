from Paciente.cl_paciente import Paciente
from Médico.cl_medico import Medico
from typing import List

class validadorHospital:
        
    def validar_existencia_paciente(self, id_paciente: int, lista_pacientes: List[Paciente]):
        for paciente in lista_pacientes:
            if paciente.id == id_paciente:
                return True
        return False

    def validar_existencia_medico(self, id_medico: int, lista_medicos: List[Medico]):
        for medico in lista_medicos:
            if medico.id == id_medico:
                return True
        return False
    
    def val_cant_usuarios(self, lista_pacientes: List[Paciente], lista_medicos: List[Medico]):
        if len(lista_pacientes) == 0:
            print("No puedes registrar una consulta, no hay pacientes.")
            return False
            
        if len(lista_medicos) == 0:
            print("Mo puedes registrar una consulta, no hay médicos.")
            return False
        
        return True