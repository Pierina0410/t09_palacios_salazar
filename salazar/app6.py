#Programa que devuelve el area del circulo

import libreria
import os

x=float(os.sys.argv[1])
y=int(os.sys.argv[2])


m=libreria.area_circulo(x,y,)
msg="El area del circulo entre {} y {} es: {}"
print(msg.format(x,y,m))
