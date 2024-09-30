from Escuela.CL_Escuela import Escuela
from Estudiantes.CL_Estudiante import Estudiante
from Maestros.CL_Maestro import Maestro
from Materias.CL_Materia import Materia
from Carrera.CL_Carrera import Carrera
from Semestre.CL_Semestre import Semestre
from Grupos.CL_Grupo import Grupo
from datetime import datetime

escuela = Escuela()

while True:
    print("""
          ----------MINDBOX----------\n
          1. Registrar estudiante
          2. Registrar maestro
          3. Registrar materia
          4. Registrar grupo
          5. Registrar horario
          6. Registrar carrera
          7. Registrar semestre
          8. Mostrar estudiantes
          9. Mostrar maestros
          10. Mostrar materias
          11. Mostrar carreras
          12. Mostrar semestres
          13. Mostrar grupos
          14. Eliminar estudiante
          15. Eliminar maestro
          16. Eliminar materia
          17. Eliminar grupo
          18. Salir""")
    
    opcion = input("\nIngresa la función a realizar: ")
    
    if opcion == "1":
        print(""""\n-----Registrar Estudiante-----\n""")
                
        nombre = input("\nIngresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la CURP del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento: "))
        dia = int(input("Ingresa el dia de nacimiento: "))
        mes = int(input("Ingresa el mes de nacimiento: \n"))
        fecha_nacimiento = datetime(ano, mes, dia)
        
        gen_num_control_estudiante = escuela.gen_num_control_estudiante()
        
        estudiante_ = Estudiante(numero_control=gen_num_control_estudiante, nombre=nombre, apellido=apellido, curp=curp, f_nacimiento=fecha_nacimiento)
        escuela.reg_estudiante(estudiante_)
        escuela.reg_estudiante(estudianteReg=estudiante_)
        

        print(f"""\nEstudiante registrado correctamente.
Número de control: {gen_num_control_estudiante}""")
        
        
    elif opcion == "2":
        print(""""\n-----Registrar Maestro-----""")
        
        nombre = input("\nIngresa el nombre del maaestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano_nacimiento = input("Ingresa el año de nacimiento: ")
        rfc = input("Ingresa el RFC del maestro: ")
        sueldo = int(input("Ingresa el sueldo: \n"))
        
        maestro_ = Maestro(numero_control="", nombre=nombre, apellido=apellido, sueldo=sueldo, rfc=rfc, ano_nacimiento=ano_nacimiento)
        gen_numero_control_maestro = escuela.gen_num_control_maestro(maestro_)
        maestro_.ma_numero_control = gen_numero_control_maestro
        escuela.reg_maestro(maestro_)
        
        print(f"""\nMaestro registrado correctamente.
Número de control: {gen_numero_control_maestro}""")
        
    elif opcion == "3":
        
        print(""""\n-----Registrar Materia-----""")
        
        nombre_materia = input("\nIngresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripción: ")
        semestre = input("Ingresa el semestre: ")
        creditos = input("Ingresa los creditos: \n")
        
        materia_ = Materia(num_materia="", nombre=nombre_materia, descripcion=descripcion, semestre=semestre, creditos=creditos)
        gen_numero_control_materia = escuela.gen_num_control_materia(materia_)
        materia_.num_c_materia = gen_numero_control_materia
        escuela.reg_materia(materia_)
        
        print(f"""\nMateria registrada correctamente.
Número de control: {gen_numero_control_materia}""")
        
    elif opcion == "4":
        print(""""\n-----Registrar grupo-----""")
        tipo = input("Ingresa el tipo de grupo (A ó B):")
        id_semestre = input("Ingresa el Id del semestre al que pertenece: \n")
        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        escuela.reg_grupo(grupo)
        print(f"""\nGrupo registrado correctamente.
ID Grupo: {grupo.ID}""")


    elif opcion == "6":
        print(""""\n-----Registrar carrera-----""")
        nombre_carrera = input("\nIngresa el nombre de la carrera: ")
        carrera = Carrera(nom_carrera=nombre_carrera)
        gen_matricula = carrera.gen_matricula(carrera)
        escuela.reg_carrera(carrera)
        print(f"""\nCarrera registrada correctamente.
              
              Matrícula: {carrera.ca_matricula}""")

    elif opcion == "7":
        print(""""\n-----Registrar semestre-----""")
        num_semestre = input("Ingresa el número de semestre: ")
        id_carrera = input("Ingresa el ID de la carrera: \n")
        _semestre =  Semestre(numero=num_semestre, id_carrera=id_carrera)
        gen_id_semestre = _semestre.gen_id_sem(_semestre)
        escuela.reg_semestre(_semestre)
        print(f"""\nSemestre registrado correctamente.
ID Semestre: {_semestre.ID}""")

    elif opcion == "8":
        escuela.listar_estudiantes()

    elif opcion == "9":
        escuela.listar_maestros()

    elif opcion == "10":
        escuela.listar_materias()

    elif opcion == "11":
        escuela.listar_carreras()

    elif opcion == "12":
        escuela.listar_semestres()

    elif opcion == "13":
        escuela.listar_grupos()

    elif opcion == "14":
        print("\n-----Eliminar estudiante-----\n")
        numero_control = input("Ingresa el número de control: ")
        escuela.eliminar_estudiante(numero_control=numero_control)
        print("-----Estudiante eliminado correctamente-----")

    elif opcion == "15":
        print("\n-----Eliminar maestro-----\n")
        numero_control = input("Ingresa el número de control: ")
        escuela.eliminar_maestro(numero_control=numero_control)
        print("-----Maestro eliminado correctamente-----")

    elif opcion == "16":
        print("\n-----Eliminar materia-----\n")
        numero_control = input("Ingresa el número de control: ")
        escuela.eliminar_materia(numero_control=numero_control)
        print("-----Materia eliminada correctamente-----")

    elif opcion == "15":
        pass
