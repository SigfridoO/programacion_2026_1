

class Madre:
    def __init__(self):
        print("Soy Madre")

    def pegar(self):
        print("Estoy pegando")

class Padre:
    def __init__(self):
        print("Soy Padre")

    def reganar(self):
        print("Estoy regañando")

class Hijo(Madre, Padre):
    # Constructor
    def __init__(self):
        #super().__init__()
        Padre.__init__(self)
        Madre.__init__(self)
        print("Soy Hijo")

def main():
    print("Iniciando el programa")
    hijo = Hijo()
    hijo.reganar()
    hijo.pegar()

if __name__ == "__main__":
    main()