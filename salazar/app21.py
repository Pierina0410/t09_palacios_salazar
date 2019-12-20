# Programa para halar el perimetro de un triangulo
import libreria
import os

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])
z=float(os.sys.argv[3])

m=libreria.perimetro(x,y,z)
msg="El perimetro de un triangulo de lados {} , {} y {} es: {}"
print(msg.format(x,y,z,m))
