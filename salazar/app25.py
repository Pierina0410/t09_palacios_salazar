# Programa para halar la excentricidad de una elipse
import libreria
import os

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])

m=libreria.exc(x,y)
msg="La excentricidad de la elipse entre los valores {} y {} es: {}"
print(msg.format(x,y,m))
