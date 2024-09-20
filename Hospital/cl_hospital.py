from typing import List
from Paciente.cl_paciente import Paciente
from Médico.cl_medico import Medico
from Consulta.cl_consultas import consulta
from validador_hospital import validadorHospital

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[consulta] = []
    validador_hospital = validadorHospital
    
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    #Registar Consulta
    def registrar_consulta(self, id_medico, id_paciente):
        if not self.validador_hospital.val_cant_usuarios(lista_medicos=self.medicos, lista_pacientes=self.pacientes):
            pass
        
        if self.val == False or self.validar_existencia_paciente(id_paciente) == False :
            print("Nose puede registrar la consulta, no existe el médico o paciente.")
            return
        
        print("Continua con el registro.")
        return 
    
    def mostrar_pacientes(self):
        print("\nPacientes en el Sistema:\n")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
            
    def mostrar_medicos(self):
        print("\nMédicos en el sistema:\n")
        for medico in self.medicos:
            medico.mostrar_informacion()
            
    def mostrar_pacientes_menores(self):
        print("\nPacientes menores en el sistema:\n")
        for paciente in self.pacientes:
            if (2024-paciente.ano_nacimiento) < 18:
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores(self):
        print("\nPacientes mayores en el sistema:\n")
        for paciente in self.pacientes:
            if (2024-paciente.ano_nacimiento) >= 18:
                paciente.mostrar_informacion()
                
    def eliminar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                self.pacientes.remove(paciente)
                print("\nPaciente con el Id ", id_paciente, " eliminado\n")
                return
        print("No se encontro paciente con id ", id_paciente, "\n")

    def eliminar_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                self.medicos.remove(medico)
                print("\nMedico con el Id ", id_medico, " eliminado\n")
                return
        print("No se encontro medico con id ", id_medico, "\n")