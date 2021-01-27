#Operadores and y or

usuario_logueado = True
usuario_admin = True
if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print('Es usuario')
else:
    print('Debes Iniciar Sesion')

if usuario_logueado or usuario_admin:
    print('entraste')