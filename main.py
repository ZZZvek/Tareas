from cl_curso import curso
from cl_estudiante import estudiante

#Buscar estudiante por ID
def buscar_ID(id):
    if estudiante_1.id_estudiante == id:
        return estudiante_1
    elif estudiante_2.id_estudiante == id:
        return estudiante_2
    else:
        return None


curso_1 = curso("Mecánica de Materiales", 10, "Daniel Cahue")
curso_2 = curso("Dinámica", 11, "Nicolás Ponciano")
curso_3 = curso("Programación avanzada", 12, "Eder Rivera")

estudiante_1 = estudiante(213243, "Juan espindola", 21)
estudiante_2 = estudiante(435465, "Vangelis Contreras", 20)


while True:
    print("\nSistema de gestión de datos escolares\n")
    print("Opciones en el sistema:\n")
    print("1. Mostrar datos de estudiante.\n")
    print("2. Agregar curso.\n")
    print("3. Salir.\n")
    
    opcion = str(input("Ingresa la operación a realizar: "))
    
    if opcion == "1":
        id_seleccionada = int(input("Ingresa el ID del alumno: "))
        estudiante_buscado = buscar_ID(id_seleccionada)
        if estudiante_buscado:
            estudiante_buscado.mostrar_info_estudiante()
        else:
            print("Estudiante no encontrado.")
    
    elif opcion == "2":
        id_seleccionada = int(input("Ingresa el ID del alumno: "))
        estudiante_buscado = buscar_ID(id_seleccionada)
        
        if estudiante_buscado:
            print("Elige un curso para asignar:")
            print("1. Mecánica de Materiales.")
            print("2. Dinámica.")
            print("3. Programación avanzada.")
            
            curso_opcion = input("Ingresa el curso a cargar: ")
            if curso_opcion == "1":
                estudiante_buscado.agregar_curso(curso_1)
            elif curso_opcion == "2":
                estudiante_buscado.agregar_curso(curso_2)
            elif curso_opcion == "3":
                estudiante_buscado.agregar_curso(curso_3)
            else:
                print("Curso no disponible.")
        else:
            print("estudiante no encontrado.")
                
    elif opcion == "3":
        print("\nHasta luego.")
        break
    
    else:
        print("Opción desconocida.")

# curso_1.mostrar_info_curso()
# curso_2.mostrar_info_curso()
# curso_3.mostrar_info_curso()
