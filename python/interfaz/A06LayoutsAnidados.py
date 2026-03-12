from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton
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
        layout_vertical_01 = QVBoxLayout()
        layout_horizontal_01 = QHBoxLayout()
        layout_horizontal_02 = QHBoxLayout()
        layout_vertical_02 = QVBoxLayout()
        layout_vertical_03 = QVBoxLayout()

        caja = Caja("Red")
        caja1 = Caja("Green")
        caja2 = Caja("#ffff00")
        caja3 = Caja("Pink")
        caja4 = Caja("Orange")
        caja5 = Caja("Blue")
        caja6 = Caja("Violet")
        titulo = QLabel("¿Quieres andar conmigo?")
        txt_si = QLabel("SI")
        txt_no = QLabel("NO")
        btn_si = QPushButton("SI QUIERE")
        btn_no = QPushButton("NO QUIERE")
        btn_aceptar = QPushButton("Aceptar")
        btn_cancelar = QPushButton("Cancelar")

        contenedor.setLayout(layout_vertical_01)

        layout_vertical_02.addWidget(txt_si)
        layout_vertical_02.addWidget(txt_no)

        layout_vertical_03.addWidget(btn_si)
        layout_vertical_03.addWidget(btn_no)
        
        layout_horizontal_01.addLayout(layout_vertical_02)
        layout_horizontal_01.addLayout(layout_vertical_03)

        layout_vertical_01.addWidget(titulo)
        layout_horizontal_02.addWidget(btn_aceptar)
        layout_horizontal_02.addWidget(btn_cancelar)
        layout_vertical_01.addLayout(layout_horizontal_01)
        layout_vertical_01.addLayout(layout_horizontal_02)

        self.setCentralWidget(contenedor)

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()