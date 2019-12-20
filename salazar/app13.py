# Programa que utiliza colocar universidad que estudias
import libreria
import os

y=str(os.sys.argv[1])

m=libreria.uni(y)
msg="Estudio en la universidad: {}"
print(msg.format(y,m))
