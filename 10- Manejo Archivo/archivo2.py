#Leer Archivos

def app():
    #otra forma de abrir el archivo con esto no hace falta cerrar el documento

    with open('./10- Manejo Archivo/Prueba.txt') as archivo:#por defecto es R de read
        for contenido in archivo:
            print(contenido.rstrip()) #para quitar los espacio podemos usar la funcion rstrip()



app()