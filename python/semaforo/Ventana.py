from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QGridLayout, QLabel, QWidget, QPushButton
from PyQt6.QtCore import QRunnable, QObject, pyqtSignal as Signal, QThreadPool
import sys

class WorkerSignals(QObject):
    luz = Signal(bool)

    def __init__(self):
        super().__init__()
class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
    
    def prender_luz(self, estado:bool):
        try:
            self.signals.luz.emit(estado)
        except Exception as e:
            print(e)

    def run(self):
        pass

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Dentro de ventana")
        contenedor = QWidget()
        mi_layout = QGridLayout()
        contenedor.setLayout(mi_layout)
        boton_arranque = QPushButton("Activar")
        boton_paro = QLabel()
        indicador = QLabel()
        mi_layout.addWidget(boton_arranque, 0, 0)
        mi_layout.addWidget(boton_paro, 1, 0)
        mi_layout.addWidget(indicador, 0, 1, 2, 1)

        self.actualizar_control(boton_arranque, "Green")
        self.actualizar_control(boton_paro, "Red")
        self.actualizar_control(indicador, "Gray")

        self.setCentralWidget(contenedor)

        self.proceso = None
        # Iniciando Worker
        self.worker = Worker()
        self.pool = QThreadPool()
        self.pool.start(self.worker)
        boton_arranque.setCheckable(True)
        boton_arranque.clicked.connect(self.cambiar_estado)

    def cambiar_estado(self, valor):
        self.cambiar_bandera_proceso(0,valor)

    def establecer_proceso(self, proceso):
        self.proceso = proceso
    
    def cambiar_bandera_proceso(self, indice:int, valor:bool):
        if self.proceso:
            self.proceso.cambiar_valor_x(indice, valor)

    def actualizar_control(self, etiqueta: QLabel, color:str):
        etiqueta.setStyleSheet(f"background-color: {color}")



def main():
    print("Iniciando el programa")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__" :
    main()