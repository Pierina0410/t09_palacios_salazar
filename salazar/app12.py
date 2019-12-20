# Programa que utiliza colocar la escuela profesional
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.carrera(x)
msg="Yo estudio la carrera profesional de: {}"
print(msg.format(x,m))
