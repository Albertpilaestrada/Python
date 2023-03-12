#!/usr/bin/env python
#_*_ coding: utf8 _*_

#if
#elif
#else

nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))

if edad == 32 and nombre == "albert":
 print("Hola {}.format(nombre)")
elif edad < 32 or nombre == "albert":
 print("Hola {}.format(nombre)")
elif not edad>=100:
 print("Nadie vive tanto jajaja")
else:
 print("Error")