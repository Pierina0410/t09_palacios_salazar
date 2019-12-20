# Programa para hallar el area de un rectangulo

import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.area_rectangulo(x,y)
msg="El area del rectangulo entre {} y {} es: {}"
print(msg.format(x,y,m))
