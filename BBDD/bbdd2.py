import sqlite3

my_conection=sqlite3.connect("GestionProductos")
my_pointer=my_conection.cursor()
my_pointer.execute('''
CREATE TABLE PRODUCTOS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
PRECIO INTEGER, 
SECCION VARCHAR(20))
''')
products=[
    ("pelota",20,"jugueteria"),
    ("pantalon",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarron",45,"ceramica")
]
my_pointer.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",products)
my_pointer.execute("INSERT INTO PRODUCTOS VALUES(NULL,'tren',15,'jugueteria')")

my_conection.commit()
my_conection.close()