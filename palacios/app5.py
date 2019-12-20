#programa para colocar el número de dni
import libreria
import os
x=str(os.sys.argv[1])
m=libreria.dni(x)
msg="EL NÚMERO DE DNI ES:{}"
print(msg.format(x,m))
