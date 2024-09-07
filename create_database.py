import sqlite3

conn = sqlite3.connect('productos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        precio_unitario REAL
    )
''')

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

cursor.executemany('''
    INSERT INTO productos (id, nombre, precio_unitario) VALUES (?, ?, ?)
''', data)

conn.commit()

