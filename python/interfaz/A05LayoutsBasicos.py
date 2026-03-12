from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QHBoxLayout, QVBoxLayout, QLabel
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        contenedor = QWidget()
        mi_layout = QHBoxLayout()
        mi_layout.setContentsMargins(10,5,20,0)
        mi_layout.setSpacing(0)

        contenedor.setLayout(mi_layout)

        caja = Caja("Red")
        caja1 = Caja("Green")
        caja2 = Caja("#ffff00")

        mi_layout.addWidget(caja)
        mi_layout.addWidget(caja1)
        mi_layout.addWidget(caja2)

        self.setCentralWidget(contenedor)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()