#Programa que devuelve una suma

import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.suma(x,y)
msg="La suma entre {} y {} es: {}"
print(msg.format(x,y,m))
