from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        mi_boton = QPushButton("Presioname")
        mi_boton.clicked.connect(self.boton_clickeado)
        mi_boton.pressed.connect(self.boton_presionado)
        mi_boton.released.connect(self.boton_liberado)
        

        self.setCentralWidget(mi_boton)

    def boton_clickeado(self):
        print("Se clickeo el boton")

    def boton_presionado(self):
        print("Se ha presionado el boton")

    def boton_liberado(self):
        print("Se ha liberado el boton")


def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()