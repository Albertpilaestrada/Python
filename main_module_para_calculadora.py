#_name_ variable privada del lenguaje
#main() funcion predefinida en el lenguaje

import modulo_calculadora as calculadora

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
            calculadora.resta(valor1,valor2)

        elif opcion==2:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            calculadora.suma(valor1,valor2)
        
        elif opcion==3:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            calculadora.multi(valor1,valor2)

        elif opcion==4:
            valor1=int(input("Valor1: "))
            valor2=int(input("Valor2: "))
            while valor2==0:
               print("Valor2 no puede ser 0\n")
               valor2=int(input("Valor2: "))            
              
            calculadora.divi(valor1,valor2)

        elif opcion==5:
            exit() 

        else:
            print("\nOpcion invalida\n")

if __name__=="__main__":
    try:
     main()
    except KeyboardInterrupt:
        print("\nSaliendo")
        exit()
