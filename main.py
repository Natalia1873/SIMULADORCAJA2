from app.controlador import Controlador



def main():
    controlador = Controlador('productos.db')
    controlador.run()


if __name__ == "__main__":
    main()
    