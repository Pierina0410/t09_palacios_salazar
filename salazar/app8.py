# Programa que utiliza colocar numero de celular
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.celular(x)
msg="El numero de celular es: {}"
print(msg.format(x,m))
