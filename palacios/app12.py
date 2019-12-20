#calcular la densidad
import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.densidad(x,y)
msg="la densidad entre {} y {} es: {}"
print(msg.format(x,y,m))
