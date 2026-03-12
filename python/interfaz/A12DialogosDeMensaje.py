from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QMessageBox, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        self.boton = QPushButton("Presioname")
        self.boton.clicked.connect(self.boton_presionado)
        self.setCentralWidget(self.boton)

    def boton_presionado(self):
        print("Se presiono el boton")
        # dialogo = QMessageBox.question(self, "Pregunta", "Realizando una pregunta")
        # dialogo = QMessageBox.warning(self, "Pregunta", "Realizando una pregunta")
        # dialogo = QMessageBox.critical(self, "Pregunta", "Realizando una pregunta")
        # dialogo = QMessageBox.information(self, "Pregunta", "Realizando una pregunta")
        dialogo = QMessageBox.about(self, "Pregunta", "Realizando una pregunta")
        
        if dialogo == QMessageBox.StandardButton.Yes:
            print("Aceptamos los cambios")
def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()