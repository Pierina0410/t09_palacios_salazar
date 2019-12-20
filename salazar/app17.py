# Programa para colocar clave WIFI
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.wifi(x)
msg="La clave de wifi es: {}"
print(msg.format(x,m))
