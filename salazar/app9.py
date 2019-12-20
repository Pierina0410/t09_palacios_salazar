# Programa que utiliza colocar nombre del rector
import libreria
import os

x=str(os.sys.argv[1])

m=libreria.celular(x)
msg="El nombre del rector es: {}"
print(msg.format(x,m))
