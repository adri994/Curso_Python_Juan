playlist ={}
playlist['canciones'] = []

#funcion principal
def app():

    #agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('Como quieres que se llame la playlist:\r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

#Agregar canciones
def agregar_canciones():
    #bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #preguntar que cancion quiere agregar
        nombre_de_playlist = playlist['nombre']  
        pregunta = f'Agrega canciones para la playlist {nombre_de_playlist}:\r\n'
        pregunta += 'Escribe "x" cuando quieras dejar de escribir canciones\r\n'

        cancion = input(pregunta)
        if cancion == "x":
            agregar_cancion = False
            #Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\r\n')
    print('Canciones:\r\n')

    for canciones in playlist['canciones']:
        print(canciones)


app()