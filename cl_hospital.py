class Hospital:
    pacientes = []
    medicos = []
    consultas = []
    
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
        return False
    
    def val_cant_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registrar una consulta, no hay pacientes.")
            return False
            
        if len(self.medicos) == 0:
            print("Mo puedes registrar una consulta, no hay médicos.")
            return False
        
        return True
        
    #Registar Consulta
    def registrar_consulta(self, id_medico, id_paciente):
        if not self.val_cant_usuarios():
            return
        
        if self.validar_existencia_medico(id_medico) == False or self.validar_existencia_paciente(id_paciente) == False :
            print("Nose puede registrar la consulta, no existe el médico o paciente.")
            return
        
        print("Continua con el registro.")
        return 
    
    def mostrar_pacientes(self):
        print("Pacientes en el Sistema")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
            
    def mostrar_medicos(self):
        print("Médicos en el sistema\n")
        for medico in self.medicos:
            medico.mostrar_informacion()
            
    def mostrar_pacientes_menores(self):
        print("-------------Pacientes menores en el sistema---------\n")
        for paciente in self.pacientes:
            if (2024-paciente.ano_nacimiento) < 18:
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores(self):
        print("-------------Pacientes mayores en el sistema---------\n")
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