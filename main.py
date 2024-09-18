from Paciente.cl_paciente import Paciente
from Hospital.cl_hospital import Hospital
from Médico.cl_medico import Medico

hospital = Hospital()

while True:
    print("-----------BIENVENIDO AL IMSS-----------")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Mostrar pacientes")
    print("4. Mostrar médicos")
    print("5. Eliminar pacientes")
    print("6. eliminar médicos")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")
    
    opcion_user = input("Selecciona la opción deseada: ")
    if opcion_user == "1":
        print("\n-----Registrar Paciente-----")
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = input("Ingresa año de nacimiento: ")
        peso = input("Ingresa el peso: ")
        estatura = input("Ingresa la estatura: ")
        direccion = input("Ingresa la dirección: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente)
        print("\nPaciente registrado correctamente.")
    
    elif opcion_user == "2":
        pass
    
    elif opcion_user == "3":
        hospital.mostrar_pacientes()
        
    elif opcion_user == "9":
        print("\nGracias, en el IMSS te cuidamos.")
        break
    
    

# paciente_1 = Paciente("Juan", 2003, 80, 1.69, "Col. Centro")
# medico_1 = Medico("Pedro", 1990, "PFC9865h6", "Las flores")

# hospital.registrar_paciente(paciente= paciente_1)
# hospital.registrar_medico(medico= medico_1)
# hospital.registrar_consulta()

# hospital.mostrar_pacientes()
