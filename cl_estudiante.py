class estudiante:
    id_estudiante = 0
    nombre_estudiante = ""
    edad = 0
    cursos = []
    
    #Constructor
    def __init__(self, id, nombre, edad):
        self.id_estudiante = id
        self.nombre_estudiante = nombre
        self.edad = edad
        self.cursos = []
        
    #Agregar curso
    def agregar_curso(self, añadir_curso):
        self.cursos.append(añadir_curso)
        print("Curso", añadir_curso.nombre_curso, "cargado.")
        
    #Mostrar información
    def mostrar_info_estudiante(self):
        print("\nNombre :", self.nombre_estudiante)
        print("ID :", self.id_estudiante)
        print("Edad :", self.edad)
        
        if self.cursos:
            print("\nCursos Asignados:")
            for curso in self.cursos:
                curso.mostrar_info_curso()
        else:
            print("No tiene cursos asignados")
        
        