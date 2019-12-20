# Programa que utiliza la funcion menor
import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.menor(x,y)
msg="El menor entre {} y {} es: {}"
print(msg.format(x,y,m)
