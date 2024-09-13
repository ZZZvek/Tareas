class curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor = ""
    
    #Constructor
    def __init__(self, nombre, codigo, instructor):
        self.nombre_curso = nombre
        self.codigo_curso = codigo
        self.instructor = instructor
        
        #Mostrar información del curso
    def mostrar_info_curso(self):
        print("Nombre del curso: ", self.nombre_curso)
        print("ID del curso: ", self.codigo_curso)
        print("Instructor del curso: ", self.instructor)