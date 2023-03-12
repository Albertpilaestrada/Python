#!/usr/bin/env python
#_*_ coding: utf8 _*_

#_name_ variable privada del lenguaje
#main() funcion predefinida en el lenguaje

def saludo(nombre,edad):
    print("Hola {} tienes: {}".format(nombre,edad))

def main():
    nombre=input("Nombre: ")
    edad=int(input("Edad: "))
    saludo(nombre,edad)
if __name__=="__main__":
    main()