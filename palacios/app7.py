#programa para colocar el número de celular
import libreria
import os
x=str(os.sys.argv[1])
m=libreria.celular(x)
msg="EL NÚMERO DE CELULAR  ES:{}"
print(msg.format(x,m))
