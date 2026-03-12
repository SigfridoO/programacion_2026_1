
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        combo = QComboBox()
        combo.addItems(['Opcion 1', 'Opcion 2', 'Opcion 3', 'Opcion 4'])
        combo.currentIndexChanged.connect(self.indice_seleccionado)
        combo.currentTextChanged.connect(self.texto_seleccionado)
        self.setCentralWidget(combo)
        self.resize(400, 50)

    def indice_seleccionado(self, indice):
        print(f"Se selecciono el indice {indice}")

    def texto_seleccionado(self, texto):
        print(f"Se selecciono el texto {texto}")

def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()