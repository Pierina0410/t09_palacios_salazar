#Hallar el perimetro de un rectangulo
import libreria
import os
x=float(os.sys.argv[1])
y=float(os.sys.argv[2])

m=libreria.perimetro(x,y)
msg="El perimetro de un rectangulo es: {}"
print(msg.format(x,y,m))
