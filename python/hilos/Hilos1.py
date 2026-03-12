
import time
import threading

class Tarea:
    def __init__(self, nombre:str, duracion:float):
        self.nombre = nombre
        self.duracion = duracion
        print(f"Creando la tarea {self.nombre}")
        self.t = threading.Thread(target=self.iniciar_tarea)
    
    def iniciar(self):
        self.t.start()

    def iniciar_tarea(self):
        print(f"Iniciando la tarea {self.nombre}")
        time.sleep(self.duracion)
        print(f"Terminando la tarea {self.nombre}")

def main():
    print("Iniciando el programa")
    tarea1 = Tarea("Realizar los circuitos electrónicos", 6)
    tarea2 = Tarea("Manufactura de la estructura", 4)
    tarea3 = Tarea("Programar", 6)

    tarea1.iniciar()
    tarea2.iniciar()
    tarea3.iniciar()
    print("finalizando el programa")

if __name__ == "__main__":
    main()

