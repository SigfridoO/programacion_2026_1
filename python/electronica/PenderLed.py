
import time
import gpiod
from  gpiod.line import Direction, Value

LED = 14
# Configuracion de GPIO
chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer = "parpadeo",
    config= {
        LED: gpiod.LineSettings(
            direction= Direction.OUTPUT, output_value=Value.INACTIVE
        )
    }
)
# Activacion de la señales
try:
    while True:
        request.set_value(LED, Value.INACTIVE)
        time.sleep(1)
        request.set_value(LED, Value.ACTIVE)
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupcion por el usuario")
finally:
        request.release()
        chip.close()