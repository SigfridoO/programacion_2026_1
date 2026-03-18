import time
import threading

class Proceso:
    def __init__(self):
        self.X = []
        self.numeroX = 8

        self.Y = []
        self.numeroY = 8

        self.M = list()
        self.numeroM = 8
        self.worker = None

        for i in range(self.numeroX):
            self.X.append(False)
        
        for i in range(self.numeroY):
            self.Y.append(False)

        for i in range(self.numeroM):
            self.M.append(False)

        self.contador = 0
        self.proceso_funcionando = False

        self.tarea = threading.Thread(target=self.run_proceso)
    
    def iniciar_tarea(self):
        self.tarea.start()

    def run_proceso (self):
        self.proceso_funcionando = True
        while self.proceso_funcionando:

            # secuencia a realizar
            self.Y[0] = ( self.X[0] or self.Y[0] ) and not self.X[1]

            if self.worker:
                # print(self.worker)
                self.worker.prender_luz(self.Y[0])

            print(f"self.Y[0]: {self.Y[0]}")
            self.contador +=1
            ##print(f"contador: {self.contador}")
            time.sleep(0.001)

    def cambiar_valor_x(self, indice:int, valor:bool):
        if indice < self.numeroX:
            self.X[indice] = valor

    def establecer_worker(self, worker):
        self.worker = worker

    def __str__(self):
        return ""
    

def main():
    proceso = Proceso()
    proceso.iniciar_tarea()

if __name__ == "__main__":
    main()

