#Calcular el promedio de un estudiante
import libreria
import os
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

m=libreria.promedio(x,y)
msg="El promedio de un estudiante con notas {} y {} es: {}"
print(msg.format(x,y,m))
