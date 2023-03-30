import sqlite3

my_conection=sqlite3.connect("GestionProductos")
my_pointer=my_conection.cursor()

my_pointer.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")
productos=my_pointer.fetchall()
print(productos)

my_pointer.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")
my_pointer.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_ARTICULO='pelota'")
productos=my_pointer.fetchall()
print(productos)

my_conection.commit()
my_conection.close()