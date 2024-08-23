import sqlite3


# Conectar a la base de datos SQLite (se creará si no existe)
conn = sqlite3.connect('productos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla 'productos'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio_unitario REAL
    )
''')

# Los datos que se agregarán a la tabla 'productos'
data = [
    (1, 'Manzana', 0.5),
    (2, 'Plátano', 0.3),
    (3, 'Naranja', 0.7),
    (4, 'Uvas', 1.2),
    (5, 'Lechuga', 0.9),
    (6, 'Zanahoria', 0.4),
    (7, 'Tomate', 0.8),
    (8, 'Patata', 0.6),
    (9, 'Cebolla', 0.5),
    (10, 'Pimiento', 1.0),
]

# Insertar los datos en la tabla 'productos'
cursor.executemany('''
    INSERT INTO productos (id, nombre, precio_unitario) VALUES (?, ?, ?)
''', data)

# Guardar los cambios
conn.commit()

# Cerrar la conexión