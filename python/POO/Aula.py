
class Aula:
    def __init__(self, ubicacion, materia):
        self.ubicacion = ubicacion
        self.materia = materia
        self.alumnos = []

    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)
        print("Se ha inscrito un alumno nuevo")

    def mostrar_alumnos(self):
        if self.alumnos:
            print ('='*10, f"Lista de alumnos inscritos a {self.materia}", '='*10,)
            for indice, alumno in enumerate (self.alumnos):
                print(f"{indice} .- {alumno}")
        else:
            print(f"No hay alumnos inscritos a {self.materia}")
    