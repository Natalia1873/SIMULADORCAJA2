import sqlite3

class Producto:
    def __init__(self, id, nombre, precio_unitario):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario


class ProductoDAO:
    def __init__(self, db_file):
        self.db_file = db_file

    def obtener_productos(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = [Producto(id=row[0], nombre=row[1], precio_unitario=row[2]) for row in cursor.fetchall()]
        conn.close()
        return productos
    
class Tiquet:
    def __init__(self, productos, carrito):
        self.productos = productos
        self.carrito = carrito
        self.total = self.calcular_total()

    def calcular_total(self):
        total = 0
        for codigo, cantidad in self.carrito.items():
            precio = next((p.precio_unitario for p in self.productos if p.id == codigo), 0)
            total += precio * cantidad
        return total