import random
from Médico.cl_medico import Medico
from Paciente.cl_paciente import Paciente

class consulta:
    id: int
    fecha_hora: str
    consultorio: str
    medico: Medico
    paciente = Paciente
    
    def __init__(self, fecha_hora: str, consultorio: str, medico: Medico, paciente: Paciente):
        self.id = random.randint(1,1000)
        self.fecha_hora = fecha_hora
        self.consultorio = consultorio
        self.fecha_medico = medico
        self.paciente = paciente