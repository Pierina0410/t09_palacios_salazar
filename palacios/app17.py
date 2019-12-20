#programa para colocar el volumen de un paralepipido
import libreria
import os
x=float(os.sys.argv[1])
y=float(os.sys.argv[2])
z=float(os.sys.argv[3])
m=libreria.volumen(x)
msg="EL VOLUMEN DEL PARALEPIPIDO ES:{}"
print(msg.format(x,y,z,m))
