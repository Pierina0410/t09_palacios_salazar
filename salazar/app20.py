# Programa para colocar la potencia de un numero
import libreria
import os

x=int(os.sys.argv[1])

m=libreria.cuadrado(x)
msg="El cuadrado del numero {} es: {}"
print(msg.format(x,m))
