#programa para colocar  la energia
import libreria
import os
x=float(os.sys.argv[1])
y=float(os.sys.argv[2])
m=libreria.energia(x)
msg="La energia  ES:{}"
print(msg.format(x,y,m))
