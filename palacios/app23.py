#Colocar la marca de una laptop
import libreria
import os
x=str(os.sys.argv[1])

m=libreria.laptop(x)
msg="La marca de la laptop es: {}"
print(msg.format(x,m))
