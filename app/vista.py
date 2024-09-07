
class Vista:
    
    def mostrar_productos(self, productos, carrito):
        print("\nSIMULADOR DE CAJA")
        print("=================")
        print("Código | Producto | Precio | Unidades | Total")
        print("-------+----------+--------+----------+----------")
        for producto in productos:
            unidades = carrito.get(producto.id, 0)
            total_producto = unidades * producto.precio_unitario
            print(f"{producto.id:<6} | {producto.nombre:<9} | {producto.precio_unitario:.2f} € | {unidades:<8} | {total_producto:.2f} €")
        print("--------+-------------+------------+----------+----------")
        print(f"\nTotal: | {self.calcular_total(carrito, productos):.2f} €")

    def calcular_total(self, carrito, productos):
        total = 0
        for codigo, cantidad in carrito.items():
            precio = next((p.precio_unitario for p in productos if p.id == codigo), 0)
            total += precio * cantidad
        return total

    def solicitar_codigo(self):
        return input("Código del producto o X para terminar compra: ")

    def solicitar_unidades(self):
        return input("Ingrese el número de unidades: ")

    def preguntar_nueva_compra(self):
        return input("¿Nueva compra? (S/N): ").strip().upper()
        