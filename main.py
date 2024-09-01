from app.controlador import Controlador
from app.controlador import Vista


def main():
    controlador = Controlador('productos.db')
    controlador.run()


if __name__ == "__main__":
    main()
    