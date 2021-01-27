pregunta = 'Agrega un numero y te dire si es par o no: \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicacion \r\n'

preguntar = True

while preguntar:

    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
        
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print('Es par')
        else:
            print('No lo es')