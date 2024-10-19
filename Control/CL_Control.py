from typing import List
from Animales import CL_Animal
from Empleados import CL_Empleado
from datetime import datetime

class Control:
    mant_CURPS: List[str]
    ids_animal: List[str]
    proceso: str
    observaciones: str
    fecha_proceso: datetime

    def __init__(self, mant_CURPS: List[str], ids_animal: List[str], proceso: str, observaciones: str, fecha_proceso: datetime):
        self.mant_CURPS = mant_CURPS
        self.ids_animal = ids_animal
        self.proceso = proceso
        self.observaciones = observaciones
        self.fecha_proceso = fecha_proceso

    def mostrar_info_control(self):
        return f"""
        Id de los animales: {', '.join(self.ids_animal)}
        CURP de los encargados de mantenimiento: {', '.join(self.mant_CURPS)}
        Fecha del proceso: {self.fecha_proceso}
        Proceso a realizar: {self.proceso}
        Observaciones: {self.observaciones}
        """
