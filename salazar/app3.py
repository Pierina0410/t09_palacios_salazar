# Programa para hallar la mitad de un numero real

import libreria
import os

x=int(os.sys.argv[1])

m=libreria.mitad(x)
msg="La mitad del nnumero {} es: {}"
print(msg.format(x,m))
