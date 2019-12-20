#programa para colocar el número de telefono fijo
import libreria
import os
x=str(os.sys.argv[1])
m=libreria.telefono_fijo(x)
msg="EL NÚMERO DE TELEFONO FIJO ES:{}"
print(msg.format(x,m))
