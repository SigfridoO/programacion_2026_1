
import time
import gpiod
from  gpiod.line import Direction, Value
import threading

class Electronica:
    def __init__(self):
        print("Dentro de la clase electrónica")
        # Pines de entrada
        self.DI_00 = 14
        self.DI_01 = 15
        self.DI_02 = 18

        # Pines de salida
        self.DO_00 = 17
        self.DO_01 = 27
        self.DO_02 = 22

        self.X = []
        for i in range (8):
             self.X.append(False)

        self.Y = []
        for i in range (8):
             self.Y.append(False)

        self.funcionando = False
        self.configurar_pines()
        self.tarea = threading.Thread(target=self.iniciar)
        self.tarea.start()

    def configurar_pines(self):
        # Configuracion de GPIO
        self.chip = gpiod.Chip("/dev/gpiochip0")
        self.request = self.chip.request_lines(
            consumer = "semaforo",
            config= {
                # Entrada Digital
                self.DI_00: gpiod.LineSettings(direction= Direction.INPUT),
                self.DI_01: gpiod.LineSettings(direction= Direction.INPUT),
                self.DI_02: gpiod.LineSettings(direction= Direction.INPUT),
                # Salida digital
                self.DO_00: gpiod.LineSettings(direction= Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_01: gpiod.LineSettings(direction= Direction.OUTPUT, output_value=Value.INACTIVE),
                self.DO_02: gpiod.LineSettings(direction= Direction.OUTPUT, output_value=Value.INACTIVE),
            }
        )

    def iniciar(self):
        self.funcionando = True
        while self.funcionando:
            # Mapeo de señales
            self.X[0] = True if self.request.get_value(self.DI_00) == Value.ACTIVE else False
            self.X[1] = True if self.request.get_value(self.DI_01) == Value.ACTIVE else False
            self.X[2] = True if self.request.get_value(self.DI_02) == Value.ACTIVE else False

            self.request.set_value(self.DO_00, Value.ACTIVE if self.Y[0] == True else Value.INACTIVE)
            self.request.set_value(self.DO_01, Value.ACTIVE if self.Y[1] == True else Value.INACTIVE)
            self.request.set_value(self.DO_02, Value.ACTIVE if self.Y[2] == True else Value.INACTIVE)
            time.sleep(0.001)

def main():
    electronica = Electronica()
    electronica.Y[0] = True

if __name__ == "__main__":
    main()
