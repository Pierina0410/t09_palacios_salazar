# Programa para halar la formula de los cuadrados
import libreria
import os

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])

m=libreria.cuadra(x,y)
msg="La formula de cuadrados entre {} y {} es: {}"
print(msg.format(x,y,m))
