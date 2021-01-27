lenguajes = ['Python','Javascript','PHP','Java']

#evaluar un elemento de una lista o array
if 'PHP' in lenguajes:
    print('Si esta en la Lista')
else:
    print('No esta en la Lista')

#if Anidados
autenticado = True
admin = False

if autenticado:
    if admin:
        print('acceso Total')
    else:
        print('Acceso Normal')
else:
    print('no puede')