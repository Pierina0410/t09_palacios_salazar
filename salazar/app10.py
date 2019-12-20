# Programa que utiliza para dividir cualquier numero real entre 3
import libreria
import os

x=float(os.sys.argv[1])

m=libreria.operacion(x)
msg="la operacion es: {}"
print(msg.format(x,m))
