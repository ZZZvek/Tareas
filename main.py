from Escuela.CL_Escuela import Escuela
from Estudiantes.CL_Estudiante import Estudiante
from Maestros.CL_Maestro import Maestro
from Materias.CL_Materia import Materia
from datetime import datetime

escuela = Escuela()

while True:
    print("""
          ----------MINDBOX----------\n
          1. Registrar estudiante
          2. Registrar maestro
          3. Registrar materia
          4. Registrar grupo
          5. Registrar Horario
          6. Salir""")
    
    opcion = input("Ingresa la función a realizar: ")
    
    if opcion == "1":
        print(""""-----Registrar Estudiante-----""")
                
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la CURP del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento: "))
        dia = int(input("Ingresa el dia de nacimiento: "))
        mes = int(input("Ingresa el mes de nacimiento: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        
        gen_num_control_estudiante = escuela.gen_num_control_estudiante()
        
        estudiante_ = Estudiante(numero_control=gen_num_control_estudiante, nombre=nombre, apellido=apellido, curp=curp, f_nacimiento=fecha_nacimiento)
        escuela.reg_estudiante(estudiante_)
        escuela.reg_estudiante(estudianteReg=estudiante_)
        

        print(f"""Estudiante registrado correctamente.
              Número de control: {gen_num_control_estudiante}""")
        
        
    elif opcion == "2":
        print(""""-----Registrar Maestro-----""")
        
        nombre = input("Ingresa el nombre del maaestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano_nacimiento = input("Ingresa el año de nacimiento: ")
        rfc = input("Ingresa el RFC del maestro: ")
        sueldo = int(input("Ingresa el sueldo: "))
        
        maestro_ = Maestro(numero_control="", nombre=nombre, apellido=apellido, sueldo=sueldo, rfc=rfc, ano_nacimiento=ano_nacimiento)
        gen_numero_control_maestro = escuela.gen_num_control_maestro(maestro_)
        maestro_.ma_numero_control = gen_numero_control_maestro
        escuela.reg_maestro(maestro_)
        
        print(f"""Maestro registrado correctamente.
              Número de control: {gen_numero_control_maestro}""")
        
    elif opcion == "3":
        
        print(""""-----Registrar Materia-----""")
        
        nombre_materia = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripción: ")
        semestre = input("Ingresa el semestre: ")
        creditos = input("Ingresa los creditos: ")
        
        materia_ = Materia(num_materia="", nombre=nombre_materia, descripcion=descripcion, semestre=semestre, creditos=creditos)
        gen_numero_control_materia = escuela.gen_num_control_materia(materia_)
        materia_.num_c_materia = gen_numero_control_materia
        escuela.reg_materia(materia_)
        
        print(f"""Materia registrada correctamente.
              Número de control: {gen_numero_control_materia}""")
        
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        break
