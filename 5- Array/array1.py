lenguaje = ['Python', 'Java','GO','Javascript']

print(lenguaje)

print(lenguaje[0])

#Ordenar list

lenguaje.sort()
print(lenguaje)
aprendido = f'Estoy aprendiendo {lenguaje[3]}'
print(aprendido)

#Modificando arreglo
lenguaje[2] = 'PHP'
print(lenguaje)

#agregar a un arreglo
lenguaje.append('GO')
print(lenguaje)

#Eliminar de un array
del lenguaje[4]
print(lenguaje)

#eliminar el ultimo elemento
lenguaje.pop()
print(lenguaje)

#Eliminar por nombre
lenguaje.remove('PHP')
print(lenguaje)

