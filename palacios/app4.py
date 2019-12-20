#programa para colocar el número de RUC
import libreria
import os
x=str(os.sys.argv[1])
m=libreria.ruc(x)
msg="EL NÚMERO DE RUC ES:{}"
print(msg.format(x,m))
