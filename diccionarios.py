#!/usr/bin/env python
#_*_ coding: utf8 _*_

#diccionarios

diccionario = dict(nombre="alumno",plataforma="ICV",edad=32)
print(diccionario["nombre"])
#diccionario = {}

#items
a=diccionario.items()
print(a)

#copy
b=diccionario.copy()
print(b)

#keys
keys=diccionario.keys()
print(keys)

#values
values=diccionario.values()
print(values)

for n in diccionario.keys():
    print("{} su valor es: {}".format(n,diccionario[n]))
