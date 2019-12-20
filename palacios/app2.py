#calcular el area cuadrado
import libreria
import os

a=int(os.sys.argv[1])
b=int(os.sys.argv[2])

m=libreria.area_triangulo(a,b)
msg="El area del triangulo entre {} y {} es: {}"
print(msg.format(a,b,m))
