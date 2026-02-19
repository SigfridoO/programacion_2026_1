from Aula import Aula
from Persona import Persona

def main():
    print("Iniciando")
    laboratorio3 = Aula("Hidraulica", "Programación")

    laboratorio3.mostrar_alumnos()

    antonio = Persona("Antonio", "Quiroz")

    laboratorio3.inscribir_alumno(antonio)
    laboratorio3.mostrar_alumnos()
    
if __name__ == '__main__':
    main()
