# Programa que utiliza sacar el promedio de 4 notas
import libreria
import os

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])
z=float(os.sys.argv[3])
w=float(os.sys.argv[4])

m=libreria.promedio(x,y,z,w)
msg="El promedio de las notas {} , {} , {} y {} es: {}"
print(msg.format(x,y,z,w,m))
