#Creando diccionario simple
cancion ={
    'artista':'Metalica',
    'cancion':'Enter Sandman',
    'lanzamiento':1992,
    'likes':2000
}

print(cancion['artista'])

#para que podamos ponerlo en una cade de texto es mejor poner en una variable  es decir
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

#Agregar a un objeto
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#Reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#eliminar un valor
del cancion['cancion']
print(cancion)