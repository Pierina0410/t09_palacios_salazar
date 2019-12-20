#Hallar la energia cinetica
import libreria
import os
x=float(os.sys.argv[1])
y=float(os.sys.argv[2])

m=libreria.energia(x,y)
msg="La energia cinetica entre {} y {} es: {}"
print(msg.format(x,y,m))
