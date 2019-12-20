#calcular el volumen de un cubo
import libreria
import os

x=int(os.sys.argv[1])


m=libreria.volumen_cubo(x,y)
msg="El volumen del cubo de {} es: {}"
print(msg.format(x,m))
