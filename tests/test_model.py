import pytest
from app.model import Producto, ProductoDAO, Tiquet

def test_producto():
    producto = Producto(id=1, nombre="Manzana", precio_unitario=0.5)

    assert producto.id == 1
    assert producto.nombre == "Manzana"
    assert producto.precio_unitario == 0.5

def test_obtener_productos():
    producto_dao = ProductoDAO('productos.db')
    productos = producto_dao.obtener_productos()

    assert len(productos) == 10 

    assert productos[0].id == 1
    assert productos[0].nombre == "Manzana"
    assert productos[0].precio_unitario == 0.5

    assert productos[1].id == 2
    assert productos[1].nombre == "Plátano"
    assert productos[1].precio_unitario == 0.3

    assert productos[2].id == 3
    assert productos[2].nombre == "Naranja"
    assert productos[2].precio_unitario == 0.7

def test_calcular_total():
    productos = [
        Producto(id=1, nombre="Manzana", precio_unitario=0.5),
        Producto(id=2, nombre="Plátano", precio_unitario=0.3),
    ]

    carrito = {1:2, 2:3}

    tiquet = Tiquet(productos, carrito)

    assert tiquet.total == 1.9

def test_calcular_total_con_productos_vacio():
    productos = [
        Producto(id=1, nombre="Manzana", precio_unitario=0.5),
        Producto(id=2, nombre="Plátano", precio_unitario=0.3),
    ]

    carrito = {}

    tiquet = Tiquet(productos, carrito)

    assert tiquet.total == 0.0


def test_calcular_total_con_productos_inexistentes():
    productos = [
        Producto(id=1, nombre="Manzana", precio_unitario=0.5),
        Producto(id=2, nombre="Plátano", precio_unitario=0.3),
    ]

    carrito = {3:1}

    tiquet = Tiquet(productos, carrito)

    assert tiquet.total == 0.0



