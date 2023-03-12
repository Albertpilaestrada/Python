#!/usr/bin/env python
#_*_ coding: utf8 _*_

#_name_ variable privada del lenguaje
#main() funcion predefinida en el lenguaje

def resta(valor1,valor2):
    print("La resta es : {}".format(valor1-valor2))

def suma(valor1,valor2):
    print("La suma es : {}".format(valor1+valor2))

def multi(valor1,valor2):
    print("La multiplicacion es : {}".format(valor1*valor2))

def divi(valor1,valor2):

    print("La division es : {}".format(valor1/valor2))

def main():
    while True:
        print("\nBienvenido\n")
        print("1.- resta dos numeros")
        print("2.- suma dos numeros")
        print("3.- multiplica dos numeros")
        print("4.- divide dos numeros")
        print("5.- Salir")

        opcion=int(input("Opcion: "))

        if opcion==1:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            resta(valor1,valor2)

        elif opcion==2:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            suma(valor1,valor2)
        
        elif opcion==3:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            multi(valor1,valor2)

        elif opcion==4:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            while valor2==0:
               print("Valor2 no puede ser 0\n")
               valor2=int(input("Valor2: "))            
              
            divi(valor1,valor2)

        elif opcion==5:
            exit() 

        else:
            print("\nOpcion invalida\n")

if __name__=="__main__":
    main()