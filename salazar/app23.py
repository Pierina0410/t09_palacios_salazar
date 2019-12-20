# Programa para halar teorema de pitagoras
import libreria
import os

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])

m=libreria.pitagoras(x,y)
msg="Teprema de pitagoras entre {} y {} es: {}"
print(msg.format(x,y,m))
