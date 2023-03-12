#!/usr/bin/env python
#_*_ coding: utf8 _*_

#classmethod
#staticmethod
#property

class prueba1(object):
    def __init__(self,radio):
        self.radio=radio
    #@classmethod #nos ayuda a usar una funcion sin que antes la clase sea atribuida a un objeto
    #def saludo(cls,nombre):
        #print("Hola {}".format(nombre))

    #@staticmethod 
    #def saludo_static():
       #print("Bienvenido")

    @property
    def area_circulo(self):
       return 3.1416*(self.radio**2)

def main():
 #nombre=input("Nombre: ") #classmethod
 #prueba1.saludo(nombre) #classmethod
 c=prueba1(5) #staticmethod
 #c.saludo_static() #staticmethod
 area=c.area_circulo
 print(area)


if __name__=="__main__":
    main()   
