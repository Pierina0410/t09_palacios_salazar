# Programa para halar la direccion de un lugar
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.direccion(x)
msg="La direccion es: {}"
print(msg.format(x,m))
