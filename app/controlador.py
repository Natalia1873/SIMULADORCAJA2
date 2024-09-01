from app.model import ProductoDAO, Producto, Tiquet 
from app.vista import Vista 


class Controlador:
    def __init__(self, db_file):
        self.dao = ProductoDAO(db_file)
        self.productos = self.dao.obtener_productos()
        self.carrito = {}
        self.vista = Vista()

    def agregar_producto(self, codigo, cantidad):
        if codigo in self.carrito:
            self.carrito[codigo] += cantidad
        else:
            self.carrito[codigo] = cantidad

    def run(self):
        while True:
            self.carrito = {} 

            while True:
                self.vista.mostrar_productos(self.productos, self.carrito)
                codigo_producto = self.vista.solicitar_codigo()

                if codigo_producto.upper() == 'X':
                    break

                try:
                    codigo = int(codigo_producto)
                    if not any(p.id == codigo for p in self.productos):
                        print("Error: Código de producto no existe.")
                        continue
                except ValueError:
                    print("Error: El código debe ser un número.")
                    continue

                unidades = self.vista.solicitar_unidades()
                try:
                    cantidad = int(unidades)
                    if cantidad < 1:
                        raise ValueError
                    self.agregar_producto(codigo, cantidad)
                except ValueError:
                    print("Error: El número de unidades debe ser un número mayor que 0.")
                    continue

            self.vista.mostrar_productos(self.productos, self.carrito)
            if self.carrito:
                tiquet = Tiquet(self.productos, self.carrito)
                print(f"Total a pagar: {tiquet.total:.2f} €")
            else:
                print("No se realizaron compras.")

            if self.vista.preguntar_nueva_compra() != 'S':
                break