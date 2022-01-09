import os


def recorridoRecursivo (mypath):
    datos2 = os.scandir(mypath)
    ficheros = []
    directorios = []
    for dato2 in datos2:
        if os.path.isfile(os.path.join(mypath, dato2)):
            ficheros.append(dato2)

        if os.path.isdir(os.path.join(mypath, dato2)):
            directorios.append(dato2)
            print(os.path.abspath(dato2))

    for fichero in ficheros:
        print('- Fichero: ', fichero, '- Tamaño', os.path.getsize(os.path.join(mypath, fichero)), 'bytes')

    for directorio in directorios:
        print(directorio)
        recorridoRecursivo(directorio)

def main ():
    pass

# Obtén todos los ficheros y directorios de un directorio en concreto.
# Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
# Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
# Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.
#Lista los tamaños de los ficheros en formato humano.

datos = os.listdir('/Users/estefaniaroblesserrano/Downloads')

for dato in datos:
    if os.path.isfile(os.path.join('/Users/estefaniaroblesserrano/Downloads', dato)):
        print('- Fichero: ', dato, '- Tamaño', os.path.getsize(os.path.join('/Users/estefaniaroblesserrano/Downloads', dato)), 'bytes')


#Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de
# cada directorio y su tamaño.

mypath = '/Users/estefaniaroblesserrano/'
recorridoRecursivo(mypath)



if __name__ == '__main__':
    main()
