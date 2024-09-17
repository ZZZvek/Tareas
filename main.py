from cl_paciente import Paciente
from cl_hospital import Hospital
from cl_medico import Medico

hospital = Hospital()
paciente_1 = Paciente("Juan", 2003, 80, 1.69, "Col. Centro")
medico_1 = Medico("Pedro", 1990, "PFC9865h6", "Las flores")

hospital.registrar_paciente(paciente= paciente_1)
hospital.registrar_medico(medico= medico_1)
hospital.registrar_consulta()

hospital.mostrar_pacientes()
