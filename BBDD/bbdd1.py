import sqlite3

my_conection=sqlite3.connect("first_database")
my_pointer=my_conection.cursor()
#my_pointer.execute("CREATE TABLE PRODUCTOS(Nombre_Articulo varchar(50), Precio integer, Seccion varchar(20))")
#my_pointer.execute("INSERT INTO PRODUCTOS VALUES('Balon',15,'Deportes')")
several_products=[
    ("Camiseta",10,"Deportes"),
    ("Jarron",55,"Ceramica"),
    ("Camion",25,"Juguetes"),
]
#my_pointer.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",several_products)
my_pointer.execute("SELECT * FROM PRODUCTOS")
several_product=my_pointer.fetchall()
for product in several_product:
    print(product)

my_conection.commit()
my_conection.close()