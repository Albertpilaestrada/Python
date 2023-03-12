#!/usr/bin/env python
#_*_ coding: utf8 _*_

#open w=write

archivo=open("archivo1.txt","w")
nombre=input("nombre: ")
edad=input("edad: ")
pais=("pais: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)

print("los datos fueron escritos")
archivo.close()
