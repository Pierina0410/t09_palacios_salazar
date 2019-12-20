#Programa que devuelve el producto de 3 numeros

import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])

m=libreria.producto(x,y,z)
msg="El producto entre {} , {} y {} es: {}"
print(msg.format(x,y,z,m))
