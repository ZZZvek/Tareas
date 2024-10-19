from datetime import datetime
from Veterinario.CL_Veterinario import Veterinario
from Zoologico.CL_Zoologico import Zoologico
from Guia.CL_Guía import Guia
from Mantenimiento.CL_Mantenimiento import Mantenimiento
from Animales.CL_Animal import Animal
from Visitantes.CL_Visitante import Visitante
from Visita.CL_Visita import Visita
from Control.CL_Control import Control


class Menú:
    zoo: Zoologico = Zoologico()

    def login(self):
        while True:

            print("+++++INICIAR SESIÓN+++++")

            usuario = input("Ingresa tu Usuario: ")
            contraseña = input("Ingresa tu contraseña: ")

            administrador = self.zoo.validar_login(usuario=usuario, contraseña=contraseña)

            if administrador is None:
                print("Usuario o contraseña inválidos.")
            else:
                self.mostrar_menú()
    
    
    def mostrar_menú(self):
        num_visitas =0
        precio = 0
        while True:
            print(
                """
    ++++++ ZOOLÓGICO ++++++

    1. Registrar Empleado (Veterinario)
    2. Registrar Empleado (Mantenimiento)
    3. Registrar Empleado (Guía)
    4. Registrar Animal
    5. Registrar Visitante
    6. Registrar Visita
    7. Registrar mantenimiento a hacer

    10. Mostrar Empleados (Veterinario)
    11. Mostrar Empleados (Mantenimiento)
    12. Mostrar Empleados (Guía)
    13. Mostrar Animales
    14. Mostrar Visitantes
    15. Mostrar Visitas
    16. Mostrar mantenimiento a hacer

    17. Eliminar Empleado (Veterinario)
    18. Eliminar Empleado (Mantenimiento)
    19. Eliminar Empleado (Guía)
    20. Eliminar Animal

    
    40. Salir
    """
            )

            opcion = int(input("\nIngresa la función a realizar: "))

            if opcion == 1:
                print("\n+++ Registrar Empleado (Veterinario) +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)
                rfc = input("Ingresa el RFC: ")
                salario = input("Ingresa el salario: ")
                horario = input("Ingresa el horario: ")

                _veterinario = Veterinario(vet_nombre=nombre,
                                        vet_apellido=apellido,
                                        vet_CURP=curp,
                                        vet_fecha_nacimiento=f_nacimiento,
                                        vet_fecha_ingreso=f_ingreso,
                                        vet_RFC=rfc,
                                        vet_salario=salario,
                                        vet_horario=horario)
                

                self.zoo.reg_veterinario(veterinarioReg=_veterinario)

            if opcion == 2:
                print("\n+++ Registrar Empleado (Mantenimineto) +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)

                rfc = input("Ingresa el RFC: ")
                salario = input("Ingresa el salario: ")
                horario = input("Ingresa el horario: ")

                _mantenimiento = Mantenimiento(mant_nombre=nombre,
                                        mant_apellido=apellido,
                                        mant_CURP=curp,
                                        mant_fecha_nacimiento=f_nacimiento,
                                        mant_fecha_ingreso=f_ingreso,
                                        mant_RFC=rfc,
                                        mant_salario=salario,
                                        mant_horario=horario)
                

                self.zoo.reg_mantenimiento(mantenimientoReg=_mantenimiento)

            if opcion == 3:
                print("\n+++ Registrar Empleado (Guía) +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)

                rfc = input("Ingresa el RFC: ")
                salario = input("Ingresa el salario: ")
                horario = input("Ingresa el horario: ")

                _guia = Guia(guia_nombre=nombre,
                             guia_apellido=apellido,
                             guia_CURP=curp,
                             guia_fecha_nacimiento=f_nacimiento,
                             guia_fecha_ingreso=f_ingreso,
                             guia_RFC=rfc,
                             guia_salario=salario,
                             guia_horario=horario)
                

                self.zoo.reg_guia(guiaReg=_guia)

            if opcion == 4:
                print("\n+++ Registrar Animal +++")
                id_animal = input("Ingresa el ID del animal: ")
                tipo_animal = input("Ingresa el tipo de animal: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento = int(input("Ingresa el año de nacimiento: "))
                f_ani_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

                dia_llegada = int(input("Ingresa el día de llegada: "))
                mes_llegada = int(input("Ingresa el mes de llegada: "))
                año_llegada = int(input("Ingresa el año de llegada: "))
                f_llegada = datetime(año_llegada, mes_llegada, dia_llegada)

                enfermedades = []
                while True:
                     enfermedad = input("Ingresa las enfermedades o fin en caso de no contar con ninguna: ")
                     if enfermedad.lower() in ["fin", "f", "nif", "fni"]:
                         break
                     enfermedades.append(enfermedad)

                tipo_alimentacion = input("Ingresa el tipo de alimentación: ")
                peso = input("Ingresa el peso del animal: ")
                frec_alimentación = input("Ingresa la frecuencia de alimentación: ")
                vacunas = input("¿Cuenta con vacunas? (s/n): ").lower() == 's'

                _animal = Animal(
                    id_animal=id_animal,
                    tipo_animal=tipo_animal,
                    fecha_llegada=f_llegada,
                    fecha_nacimiento=f_ani_nacimiento,
                    enfermedades=enfermedades,
                    tipo_alimentacion=tipo_alimentacion,
                    peso=peso,
                    frecuencia_alimentacion=frec_alimentación,
                    vacunas=vacunas
                )


                self.zoo.reg_animal(animalReg=_animal)

            if opcion == 5:
                print("\n+++ Registrar Visitante +++")
                nombre = input("\nIngresa el nombre: ")
                apellido = input("Ingresa los apellidos: ")
                curp =  input("Ingresa la CURP: ")

                dia_nacimiento = int(input("Ingresa el día de nacimiento: "))
                mes_nacimiento = int(input("Ingresa el mes de nacimiento: "))
                año_nacimiento_vis = int(input("Ingresa el año de nacimiento: "))
                f_nacimiento = datetime(año_nacimiento_vis, mes_nacimiento, dia_nacimiento)
                dia_ingreso = int(input("Ingresa el día de ingreso: "))
                mes_ingreso = int(input("Ingresa el mes de ingreso: "))
                año_ingreso = int(input("Ingresa el año de ingreso: "))
                f_ingreso = datetime(año_ingreso, mes_ingreso, dia_ingreso)

                _visitante = Visitante(
                    vi_nombre=nombre,
                    vi_apellido=apellido,
                    vi_CURP=curp,
                    vi_fecha_nacimiento=f_nacimiento,
                    vi_fecha_reg=f_ingreso,
                    vi_num_visitas=num_visitas)
                
                if (datetime.now().year) - (año_nacimiento_vis) >= 18:

                    self.zoo.reg_visitante_mayor(visitanteReg=_visitante)

                else:

                    self.zoo.reg_visitante_niños(visitanteReg=_visitante)
                
            if opcion == 6:
                print("\n+++ Registrar Visita +++")
                guia_CURPS = input("Ingrese el/los CURP de los guías (Separados por comas): ").split(",")
                vi_CURPS = input("Ingrese el/los CURP de los visitantes (Separados por comas): ").split(",")
                self.zoo.reg_visita(guia_CURPS, vi_CURPS)

            if opcion == 7:
                print("\n+++ Registrar mantenimiento a hacer +++")
                mant_CURPS = input("Ingrese el/los CURP de los empleados de mantenimiento (Separados por comas): ").split(",")
                ids_animal = input("Ingrese el/los ID de los animales (Separados por comas): ").split(",")
                proceso = input("Ingrese el proceso a realizar: ")
                observaciones = input("Ingrese las observaciones: ")
                _control = Control(
                    mant_CURPS=mant_CURPS, 
                    ids_animal=ids_animal,
                    proceso=proceso,
                    observaciones=observaciones,
                    fecha_proceso=datetime.now()
                )
                self.zoo.reg_control(_control)

            if opcion == 10:
                self.zoo.mostrar_veterinarios()
                pass

            if opcion == 11:
                self.zoo.mostrar_mantenimientos()
                pass

            if opcion == 12:
                self.zoo.mostrar_guias()
                pass
            
            if opcion == 13:
                self.zoo.mostrar_animales()
                pass

            if opcion == 14:
                self.zoo.mostrar_visitantes()
                pass

            if opcion == 15:
                self.zoo.mostrar_visitas()

            if opcion == 16:
                self.zoo.mostrar_controles()

            if opcion == 17:
                print("\n+++ Eliminar veterinario +++")
                vet_curp = input("Ingrese el CURP del veterinario que desees eliminar: ")
                self.zoo.eliminar_veterinario(vet_CURP_eliminar=vet_curp)
                pass

            if opcion == 18:
                print("\n+++ Eliminar empleado de mantenimiento +++")
                mant_CURP = input("Ingresa la CURP del empleado de mantenimiento que desees eliminar: ")
                self.zoo.eliminar_mantenimiento(mant_CURP_eliminar=mant_CURP)

            if opcion == 19:
                print("\n+++ Eliminar guía +++")
                guia_CURP_eliminar= input("Ingresa la CURP del guia que desees eliminar: ")
                self.zoo.eliminar_guia(guia_CURP_eliminar=guia_CURP_eliminar) 

                
            if opcion == 20:
                print("\n+++ Eliminar animal +++")
                id_animal_eliminar= input("Ingrese el ID del animal que desees eliminar: ")
                self.zoo.eliminar_animal(id_animal_eliminar=id_animal_eliminar)
                pass
            
            if opcion == 40:
                break
