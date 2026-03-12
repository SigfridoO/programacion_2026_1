from PyQt6.QtWidgets import ( QApplication, QMainWindow, QGridLayout,                            
    QWidget)
import sys

from Utils import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        mi_layout = QGridLayout()
        contenedor = QWidget()
        contenedor.setLayout(mi_layout)

        caja1 = Caja("Blue")
        caja2 = Caja("Orange")
        caja3 = Caja("Purple")
        caja4 = Caja("Green")

        mi_layout.addWidget(caja1, 0,0)
        mi_layout.addWidget(caja2, 1,1)
        mi_layout.addWidget(caja3, 0, 2, 2, 1)
        mi_layout.addWidget(caja4, 2, 1, 1, 2)

        mi_layout.setVerticalSpacing(5)
        mi_layout.setHorizontalSpacing(0)
        mi_layout.setContentsMargins(0, 20, 15, 10)

        print("Dentro de ventana")
        self.setCentralWidget(contenedor)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()