#!/usr/bin/env python
#_*_ coding: utf8 _*_

#_name_ variable privada del lenguaje
#main() funcion predefinida en el lenguaje

class Carro(object):
    def __init__(self,m):
        self.color="rojo"
        self.puertas=4
        self.tipo="deportivo"
        self.m=m

    def movilidad(self):
        if self.m==True:
            print("Acelerar")
        else:
            print("Frenar")


def main():
    while True:
        print("1 Acelerar")
        print("2 Frenar")
        valor=int(input("> "))
        if valor==1:
            c=Carro(True)
            c.movilidad()
        else:
            c=Carro(False)
            c.movilidad()
if __name__=="__main__":
    main()