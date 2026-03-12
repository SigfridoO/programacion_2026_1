from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, \
    QLabel, QSpinBox, QDoubleSpinBox, QGridLayout
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        contenedor = QWidget()
        mi_layout = QGridLayout()
        contenedor.setLayout(mi_layout)

        etiqueta_datos = QLabel("Datos")
        etiqueta_temperatura = QLabel("Temperatura")
        etiqueta_humedad = QLabel("Humedad")
        etiqueta_brillo = QLabel("Brillo")

        spin_temperatura = QDoubleSpinBox()
        spin_humedad = QDoubleSpinBox()
        spin_brillo = QSpinBox()

        mi_layout.addWidget(etiqueta_datos, 0, 0, 1, 2)
        mi_layout.addWidget(etiqueta_temperatura, 1, 0)
        mi_layout.addWidget(etiqueta_humedad, 2, 0)
        mi_layout.addWidget(etiqueta_brillo, 3, 0)
        mi_layout.addWidget(spin_temperatura, 1, 1)
        mi_layout.addWidget(spin_humedad, 2, 1)
        mi_layout.addWidget(spin_brillo, 3, 1)

        spin_temperatura.valueChanged.connect(self.valor_cambiado)
        # spin_temperatura.setMaximum(200)
        # spin_temperatura.setMinimum(-25)
        spin_temperatura.setRange(-10, 20)
        spin_temperatura.setPrefix("temp ")
        spin_temperatura.setSuffix(" ºC")
        spin_temperatura.setSingleStep(2.5)

        
        self.setCentralWidget(contenedor)
        self.resize(200, 150)

    def valor_cambiado(self, valor):
        print(f"Valor {valor}")




def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()