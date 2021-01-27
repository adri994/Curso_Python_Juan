#nombre = input('Cual es tu nombre: \r\n') #eso es un salto de linea
#print(f'Hola,{nombre}')

#Leer datos que son numeros
#edad = input('Cual es tu edad: \r\n')
#convertir de string a int
#edad = int(edad)

#if edad >= 18:
    #print('Puedes votar')
#else:
    #print('No puedes votar')

#Mezclarlo con operadores
""" numero = input('Agrega un numero y te dire si es par o no')
numero = int(numero)

if numero % 2 == 0:
    print('Es par')
else:
    print('No lo es') """

#Ejercicio de prueba

calificacion = 0



print('Solo responde con si o no')
pregunta1 = input('Es SNK el mejor Anime del mundo: \r\n')
resp1 = pregunta1.lower()

if resp1 == 'si':
    calificacion += 1

pregunta2 = input('Es SNK el mejor Anime del mundo: \r\n')
resp2 = pregunta2.lower()

if resp2 == 'si':
    calificacion += 1

pregunta3 = input('Es SNK el mejor Anime del mundo: \r\n')
resp3 = pregunta3.lower()

if resp3 == 'si':
    calificacion += 1

print(f'Tu calificacion es {calificacion}')