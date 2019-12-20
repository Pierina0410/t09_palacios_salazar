#calcular el area del circulo
import libreria
import os

c=int(os.sys.argv[1])
d=int(os.sys.argv[2])

m=libreria.area_circulo(c,d)
msg="El area del circulo entre {} y {} es: {}"
print(msg.format(c,d,m))
