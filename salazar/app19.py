# Programa para colocal el numero de imei
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.imei(x)
msg="El imei del celular es: {}"
print(msg.format(x,m))
