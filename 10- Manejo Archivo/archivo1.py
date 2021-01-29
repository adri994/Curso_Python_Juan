#crear y escribir archivo

def app():
    #Crear archivo
    archivo = open('./10- Manejo Archivo/Prueba.txt','w')# W es escritura, si no existe lo creara

    #Generar numeros en archivo
    for i in range(0,20):
        archivo.write(f'Esta es la linea {str(i)}\r')
    
    #Es buena practica cerrar el archivo
    archivo.close()


app()