
from PyQt6.QtWidgets import QApplication
import sys

from Ventana import Ventana
from Proceso import Proceso

class Inicio(Ventana):
    def __init__(self):
        super().__init__()
        proceso = Proceso()
        proceso.iniciar_tarea()
        self.establecer_proceso(proceso)


def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Inicio()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()