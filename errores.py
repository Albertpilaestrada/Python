#!/usr/bin/env python
#_*_ coding: utf8 _*_

try:
  while True:
   print("Hola")
#except NameError:
  #print("L no esta definida")
except KeyboardInterrupt:
  print("Salida forzosa")
finally:
  print("Termino la ejecucion")