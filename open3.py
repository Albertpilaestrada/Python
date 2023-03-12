#!/usr/bin/env python
#_*_ coding: utf8 _*_

#open

archivo=open("archivo1.txt","a")
dedicacion=input("dedicacion: ")
empresa=input("empresa: ")
idioma=input("idioma: ")

archivo.write("\n")
archivo.write(dedicacion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")
archivo.write(idioma)

archivo.close()