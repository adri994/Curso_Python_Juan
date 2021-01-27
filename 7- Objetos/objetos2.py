#iniciar obejto vacio
jugador = {}

# Agregar un valor
jugador['nombre'] = 'Adrian'
jugador['puntaje'] = 0
print(jugador)

#Incremntando puntaje
jugador['puntaje'] = 100
print(jugador)

#acceder a un valor
print(jugador.get('consola','No existe eso')) #lo hacemos cuando no esta en el objeto y ponemos esto para poner un mensaje distinto al que pone Python

#iterar en el objeto
for llave,valor in jugador.items():
    print(llave)
    print(valor)

#elimianr usuarios
del jugador['nombre']
del jugador['puntaje']
print(jugador)