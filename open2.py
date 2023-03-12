#!/usr/bin/env python
#_*_ coding: utf8 _*_

#open r=read

archivo=open("wordlist.lst","r")

#print(archivo.readlines())

lista=archivo.read().split("\n")
for n in lista():
    print(n)

for l in archivo.read().split("\n"):
    print(l)