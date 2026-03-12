from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QFileDialog, QInputDialog, QColorDialog, QFontDialog, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        self.boton = QPushButton("Presioname")
        self.setCentralWidget(self.boton)
        self.boton.clicked.connect(self.mostrar_dialog)

    def mostrar_dialog(self):
        print("Se presiono el botón")
        # archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", ".")
        # archivo, _ = QFileDialog.getSaveFileName(self, "Gurdar Archivo", ".")
        # print(archivo)

        # valor, confirmado = QInputDialog.getText(self, "Se leera texto", "texto")
        # valor, confirmado = QInputDialog.getInt(self, "Se leera un entero", "numero")
        # valor, confirmado = QInputDialog.getDouble(self, "Se leera un numero decimal", "numero", max=50, min=-10)
        # valor, confirmado = QInputDialog.getItem(self, 
        #             "Se seleccionara un elemento", 
        #             "colores", 
        #             ['Rojo', 'Verde', 'Azul'], 
        #             editable=False)
        
        # print(valor, confirmado)

        # fuente, confirmado = QFontDialog.getFont(self)
        # if confirmado:
        #     self.boton.setFont(fuente)

        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f"background-color: {color.name()}")


def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()