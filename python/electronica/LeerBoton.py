
import time
import gpiod
from  gpiod.line import Direction, Value

DI_00 = 17
DO_00 = 14

# Configuracion de GPIO
chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer = "parpadeo",
    config= {
         # Entrada Digital
        DI_00: gpiod.LineSettings(direction= Direction.INPUT),
        # Salida digital
        DO_00: gpiod.LineSettings(direction= Direction.OUTPUT, output_value=Value.INACTIVE)
    }
)
# Activacion de la señales
try:
    while True:
        valor = request.get_value(DI_00)
        print(valor)
        request.set_value(DO_00, valor)
        time.sleep(0.001)
        # request.set_value(DO_00, request.get_value(DI_00))
except KeyboardInterrupt:
    print("Interrupcion por el usuario")
finally:
        request.release()
        chip.close()