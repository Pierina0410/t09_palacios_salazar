#calcular el perimetro de una casa rectangular
import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.perimetro_rectangulo(x,y)
msg="El perimetro del rectangulo entre {} y {} es: {}"
print(msg.format(x,y,m))
