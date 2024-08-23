
## Creacion la base de datos con los productos
1. Se importan las bibliotecas sqlite3 para manejar la base de datos.
2. Se establece una conexión a una base de datos SQLite llamada productos.db (el archivo no existe, se creará automáticamente).
3. Se crea un cursor que permite ejecutar comandos SQL en la base de datos. 
4. Se ejecuta un comando SQL para crear la tabla productos. La tabla tiene tres columnas: id (un identificador único para cada producto), nombre (el nombre del producto), y precio_unitario (el precio del producto).
5. Se definen los datos que se van a insertar en la tabla productos.
6. Se utilizan los datos previamente definidos para insertar múltiples registros en la tabla productos de forma eficiente con executemany.
7. Se guardan los cambios realizados en la base de datos.
8. Se cierra la conexión a la base de datos.

