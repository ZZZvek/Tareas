from typing import List
from Guia.CL_Guía import Guia
from Visitantes.CL_Visitante import Visitante
from datetime import datetime

class Visita:
    # costo_total: float
    cant_ninos: int
    cant_adul: int
    fecha_visita: datetime
    costo_total: float
    guia_CURPS: List[Guia] = []
    visitantes: List[Visitante] = []

    def __init__(self, cant_ninos: int, cant_adul: int, fecha_visita: datetime, guia_CURPS: List[str], vi_CURPS: List[str], costo_total:float):
        # self.costo_total = costo_total
        self.cant_ninos = cant_ninos
        self.cant_adul = cant_adul
        self.fecha_visita = fecha_visita
        self.guia_CURPS = guia_CURPS
        self.vi_CURPS = vi_CURPS
        self.costo_total=costo_total
        
    def mostrar_info_visita(self):
        return f"""
        Cantidad de niños: {self.cant_ninos}
        Cantidad de adultos: {self.cant_adul}
        Fecha de la visita: {self.fecha_visita}
        Guía: {', '.join(self.guia_CURPS)}
        Visitantes: {', '.join(self.vi_CURPS)}
        Costo: {self.costo_total}
        """
    
    def registrar_visitantes(self, visitantes: List[Visitante]):
        for visitante in visitantes:
            visitante.incrementar_visitas()

    