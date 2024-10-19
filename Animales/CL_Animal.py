from datetime import datetime

class Animal:
    id_animal: str
    tipo_animal:str
    fecha_llegada: datetime
    enfermedades: str
    tipo_alimentacion: str
    fecha_nacimiento: datetime
    peso: str
    frecuencia_alimentacion: str
    vacunas: bool

    def __init__(self, id_animal: str, tipo_animal: str, fecha_llegada: datetime, enfermedades: list[str], tipo_alimentacion: str, fecha_nacimiento:str, peso:str, frecuencia_alimentacion:str, vacunas:bool):
        self.id_animal = id_animal
        self.tipo_animal = tipo_animal
        self.fecha_llegada = fecha_llegada
        self.enfermedades = enfermedades
        self.tipo_alimentacion = tipo_alimentacion
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.vacunas = vacunas

    def mostrar_info_animal(self):
        info_animal = f"Tipo de animal: {self.tipo_animal}\n"
        info_animal += f"Fecha de llegada: {self.fecha_llegada}\n"

        info_animal += "Enfermedades: "
        if self.enfermedades:
            for enfermedad in self.enfermedades:
                info_animal += enfermedad + "\n"

        info_animal += f"Tipo de alimentacion: {self.tipo_alimentacion}\n"
        info_animal += f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
        info_animal += f"Peso: {self.peso}\n"
        info_animal += f"Frecuencia de alimentacion: {self.frecuencia_alimentacion}\n"
        info_animal += f"Vacunas: {'Sí' if self.vacunas else 'No'}\n"

        return info_animal