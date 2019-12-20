# Programa para hallar la resta
import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.resta(x,y)
msg="La resta entre {} y {} es: {}"
print(msg.format(x,y,m))
