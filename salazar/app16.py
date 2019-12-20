# Programa para colocar numero de ruc
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.ruc(x)
msg="El numero de ruc es: {}"
print(msg.format(x,m))
