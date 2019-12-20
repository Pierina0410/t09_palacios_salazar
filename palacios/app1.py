#calcular el area de un triangulo
import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.area_triangulo(x,y)
msg="El area del triangulo entre {} y {} es: {}"
print(msg.format(x,y,m))
