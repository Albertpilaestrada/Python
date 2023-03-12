#!/usr/bin/env python
#_*_ coding: utf8 _*_

#for 0 bucle

mensaje = input("mensaje: ")
numero = int(input("numero: "))

for m in range(0,numero):
    #print(mensaje)
    print("{} : {}".format(m,mensaje))