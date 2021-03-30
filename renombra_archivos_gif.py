import glob
import os
# RENOMBRA VARIOS ARCHIVOS 

dir = "Ruta/De/Archivo/Para/Renombrar/"

# IMPRIME LA CANTIDAD DE ARCHIVOS .gif DEL DIRECTORIO:  
CountFicheros = len(glob.glob1(dir,"*.gif"))
#------------------------------------------------------

# RECORRE E IMPRIME NOMBRES DE ARCHIVOS .gif DEL DIRECTORIO:-------------------
contenido = os.listdir(dir)
Fichero_gif = []
for fichero in contenido:
    if os.path.isfile(os.path.join(dir, fichero)) and fichero.endswith('.gif'):
        Fichero_gif.append(fichero) # AGREGA LOS ARCHIVOS .GIF A LA LISTA
print(Fichero_gif) # IMPRIME LOS ARCHIVOS .GIF
#------------------------------------------------------------------------------

# RENOMBRAMOS LOS n ARCHIVOS gif
renombre = "renombrado"

i=1
e=1
while i<=CountFicheros:
    os.rename(dir+str(Fichero_gif[e]),dir+renombre+str(i)+".gif")
    print("Renombrado : ",i)
    i=i+1
    e=e+1



# RENOMBRA UN SOLO ARCHIVO --------------------------------------------------------------------------
# os.rename("ruta/Archivo/Anterior/archivo.txt","Ruta/Donde/Guarda/Archivo/Renombrado/renombrado.txt")
#----------------------------------------------------------------------------------------------------