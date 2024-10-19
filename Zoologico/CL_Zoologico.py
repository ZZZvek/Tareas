from datetime import datetime
from Empleados.CL_Empleado import Empleado
from Guia.CL_Guía import Guia
from Usuarios.CL_Usuario import Usuario
from Veterinario.CL_Veterinario import Veterinario
from Mantenimiento.CL_Mantenimiento import Mantenimiento
from Animales.CL_Animal import Animal
from Visitantes.CL_Visitante import Visitante
from Visita.CL_Visita import Visita
from Control.CL_Control import Control
from Director.CL_Director import Director
from typing import List

class Zoologico:

    lista_usuarios: List[Usuario] = []
    lista_empleados: List[Empleado] = []

    lista_veterinarios: List[Veterinario] = []
    lista_director: List[Director] = []
    lista_mantenimiento: List[Mantenimiento] = []
    lista_guias: List[Guia] = []
    lista_animales: List[Animal] = []
    lista_visitantes_adultos: List[Visitante] = []
    lista_visitantes_niños: List[Visitante] = []
    lista_visitas: List[Visita] = []
    lista_controles: List[Control] = []

    def __init__(self):

        director = Director(
            dir_nombre="Kevin",
            dir_apellido="García",
            dir_CURP="GAHK",
            dir_fecha_nacimiento=datetime(2003,12,20),
            dir_contraseña="1234",
            dir_nom_usuario="ZZZ",
        )
        self.lista_director.append(director)

        visitante_1 = Visitante(
            vi_nombre = "Patty",
            vi_apellido = "Aguado",
            vi_fecha_nacimiento = datetime(2004, 9, 7),
            vi_CURP = "ANAPAT001",
            vi_num_visitas = 1,
            vi_fecha_reg = datetime(2024, 1, 1)
            )
        self.lista_visitantes_adultos.append(visitante_1)
        
        visitante_2 = Visitante(
            vi_nombre = "Carlos",
            vi_apellido = "Rubio",
            vi_fecha_nacimiento = datetime(2010, 7, 7),
            vi_CURP = "JACOBO002",
            vi_num_visitas = 4,
            vi_fecha_reg = datetime(2023, 1, 1)
            )
        self.lista_visitantes_niños.append(visitante_2)

        guia_1 = Guia(
            guia_nombre = "Miguel",
            guia_apellido = "Lemus",
            guia_CURP = "MILEM001",
            guia_fecha_nacimiento = datetime(2003, 8, 28),
            guia_fecha_ingreso = datetime(2020, 1, 1),
            guia_RFC = "LEMUSPAPU",
            guia_salario = 9.99,
            guia_horario = "09 a.m. - 11 p.m."
            )
        self.lista_guias.append(guia_1)
        
        guia_2 = Guia(
            guia_nombre = "Ian",
            guia_apellido = "Cortés",
            guia_CURP = "CORIAN002",
            guia_fecha_nacimiento = datetime(2003, 5, 21),
            guia_fecha_ingreso = datetime(2021, 2, 2),
            guia_RFC = "CORTESPAPU",
            guia_salario = 99.99,
            guia_horario = "09 a.m. - 07 p.m."
            )
        self.lista_guias.append(guia_2)
        
        mantenimiento_1 = Mantenimiento(
            mant_nombre = "Vangelis",
            mant_apellido = "Contreras",
            mant_CURP = "CONT001",
            mant_fecha_nacimiento = datetime(2003, 1, 13),
            mant_fecha_ingreso = datetime(2023,3,3),
            mant_RFC = "CONTPAPU",
            mant_salario = 8,
            mant_horario = "12 a.m. - 12 p.m."
        )
        self.lista_mantenimiento.append(mantenimiento_1)

    def reg_veterinario(self, veterinarioReg: Veterinario):
        self.lista_empleados.append(veterinarioReg)
        self.lista_usuarios.append(veterinarioReg)
        self.lista_veterinarios.append(veterinarioReg)

    def reg_mantenimiento(self, mantenimientoReg: Mantenimiento):
        self.lista_empleados.append(mantenimientoReg)
        self.lista_usuarios.append(mantenimientoReg)
        self.lista_mantenimiento.append(mantenimientoReg)

    def reg_guia(self, guiaReg: Guia):
        self.lista_empleados.append(guiaReg)
        self.lista_usuarios.append(guiaReg)
        self.lista_guias.append(guiaReg)

    def reg_animal(self, animalReg: Animal):
        self.lista_animales.append(animalReg)

    def reg_visitante_mayor(self, visitanteReg: Visitante):
        self.lista_visitantes_adultos.append(visitanteReg)
        self.lista_usuarios.append(visitanteReg)

    def reg_visitante_niños(self, visitanteReg: Visitante):
        self.lista_visitantes_niños.append(visitanteReg)
        self.lista_usuarios.append(visitanteReg)

    def reg_visita(self, guias_CURPS: str, vi_CURPS: list):

        fecha_visita = datetime.now()
        
        guias_encontrados = []

        for guia_CURP in guias_CURPS:

            encontrado = False

            for guia in self.lista_guias:
                if guia.CURP == guia_CURP:
                    guias_encontrados.append(guia)
                    encontrado = True

            if not encontrado:
                print(f"El guia con CURP {guia_CURP} no está registrado.")

        visitantes_encontrados = []
        cant_ninos = 0
        cant_adul = 0
        costo_total_ni= 0
        costo_total_adul = 0

        for vi_CURP in vi_CURPS:

            encontrado = False

            for visitante in self.lista_visitantes_adultos + self.lista_visitantes_niños:
                if visitante.CURP == vi_CURP:
                    
                    visitantes_encontrados.append(visitante)
                    if visitante in self.lista_visitantes_adultos:
                        cant_adul += 1
                        costo_total_adul = 100
                        encontrado = True
                        visitante.incrementar_visitas()
                        
                        if visitante.num_visitas%5 == 0:
                            costo_total_adul = visitante.descuento() * 100
                            
                    else:
                        cant_ninos += 1
                        encontrado = True
                        visitante.incrementar_visitas()
                        costo_total_ni = 50
                        
                        if visitante.num_visitas%5 == 0:
                            costo_total_ni = visitante.descuento() * 50
                    
      
                    costo_total=costo_total_adul + costo_total_ni      
            if not encontrado:
                print(f"El visitante con CURP {vi_CURP} no está registrado.")
        
        


        if len(visitantes_encontrados) > 0:

            nueva_visita = Visita(
                cant_ninos=cant_ninos,
                cant_adul=cant_adul,
                fecha_visita=fecha_visita,
                guia_CURPS=[guia.CURP for guia in guias_encontrados],
                vi_CURPS=[visitante.CURP for visitante in visitantes_encontrados],
                costo_total=costo_total)
        
            self.lista_visitas.append(nueva_visita)
            print(f"Visita registrada exitosamente con {cant_ninos} niños y {cant_adul} adultos.")

        else:
            print("No se puede realizar la visita, no hay visitantes registrados.")

    def reg_control(self, controlReg: Control):
        fecha_proceso = datetime.now()

        mantenimientos_encontrados = []
        for mant_CURP in controlReg.mant_CURPS:
            encontrado = False
            for mantenimiento in self.lista_mantenimiento:
                if mantenimiento.CURP == mant_CURP:
                    mantenimientos_encontrados.append(mantenimiento)
                    encontrado = True
            if not encontrado:
                print(f"El empleado de mantenimiento con CURP {mant_CURP} no está registrado.")

        animales_encontrados = []
        for id_animal in controlReg.ids_animal:
            encontrado = False
            for animal in self.lista_animales:
                if animal.id_animal == id_animal:
                    animales_encontrados.append(animal)
                    encontrado = True
            if not encontrado:
                print(f"El animal con ID {id_animal} no está registrado.")

        if len(mantenimientos_encontrados) > 0 and len(animales_encontrados) > 0:
            nuevo_control = Control(
                mant_CURPS=[mantenimiento.CURP for mantenimiento in mantenimientos_encontrados],
                ids_animal=[animal.id_animal for animal in animales_encontrados],
                proceso=controlReg.proceso,
                observaciones=controlReg.observaciones,
                fecha_proceso=fecha_proceso
            )
            self.lista_controles.append(nuevo_control)
            print("Mantenimiento registrado exitosamente.")
        else:
            print("No se pudo registrar el mantenimiento, verifica los datos ingresados.")
  
    
    def mostrar_veterinarios(self):
        print("\n+++ VETERINARIOS +++\n")
        for veterinario in self.lista_veterinarios:
            print(veterinario.mostrar_info_empleado())

        
    def mostrar_mantenimientos(self):
        print("\n+++ MANTENIMIENTO +++\n")
        for mantenimiento in self.lista_mantenimiento:
            print(mantenimiento.mostrar_info_empleado())

        
    def mostrar_guias(self):
        print("\n+++ GUÍAS +++\n")
        for guia in self.lista_guias:
            print(guia.mostrar_info_empleado())

        
    def mostrar_animales(self):
        print("\n+++ ANIMALES +++\n")
        for animal in self.lista_animales:
            print(animal.mostrar_info_animal())


    def mostrar_visitantes(self):
        print("\n+++ VISITANTES +++\n")
        for visitante in self.lista_visitantes_adultos:
            print("+++ ADULTOS +++")
            print(visitante.mostrar_info_visitante())

        for visitante in self.lista_visitantes_niños:
            print("\n+++ NIÑOS +++\n")
            print(visitante.mostrar_info_visitante())


    def mostrar_visitas(self):
        print("\n+++ VISITAS +++\n")
        for visita in self.lista_visitas:
            print(visita.mostrar_info_visita())

    def mostrar_controles(self):
        print("\n+++ MANTENIMIENTOS A HACER +++\n")
        for control in self.lista_controles:
            print(control.mostrar_info_control())

    def validar_login(self, usuario:str, contraseña:str):
        for director in self.lista_director:
            if director.nom_usuario == usuario:
                if director.contraseña == contraseña:
                    return director
        return None
    pass

    def eliminar_veterinario(self, vet_CURP_eliminar:str):
        for veterinario in self.lista_veterinarios:
            if veterinario.CURP == vet_CURP_eliminar:
                self.lista_veterinarios.remove(veterinario)
                print("Veterinario eliminado correctamente.")
                return
        print("No se encontró al veterinario con esa CURP.")
    

    def eliminar_guia(self, guia_CURP_eliminar:str):
        for guia in self.lista_guias:
            if guia.CURP == guia_CURP_eliminar:
                self.lista_guias.remove(guia)
                
                print("Guía eliminado correctamente.")
                return
        print("No se encontró al guía con esa CURP.")

    def eliminar_mantenimiento(self, mant_CURP_eliminar:str):
        for mantenimiento in self.lista_mantenimiento:
            if mantenimiento.CURP == mant_CURP_eliminar:
                self.lista_mantenimiento.remove(mantenimiento)
                print("Empleado de mantenimiento eliminado.")
                return
        print("No se encomtro empleado de mantenimiento con esa CURP.")
    
    
    def eliminar_animal(self, id_animal_eliminar:str):
        for animal in self.lista_animales:
            if animal.id_animal == id_animal_eliminar:
                self.lista_animales.remove(animal)
                print("Animal eliminado.")
                return
        print("No se encontro al animal con esa ID.")