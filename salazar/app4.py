# Programa que utiliza la funcion mayor
import libreria
import os

w=int(os.sys.argv[1])
z=int(os.sys.argv[2])

m=libreria.mayor(w,z)
msg="El mayor entre {} y {} es: {}"
print(msg.format(w,z,m))
