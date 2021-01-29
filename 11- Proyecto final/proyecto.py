#Para crear un directorio necesitas importar una libreria
import os

CARPETA = './11- Proyecto final/contactos/' #se pone es mayuscula para dar a entender que es una cosntante
EXTENSION = '.txt'


#Clase Contacto
class Contacto:
    def __init__(self,nombre,telefono,categoria):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__categoria = categoria
    
    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_categoria(self):
        return self.__categoria


#funcion principal
def app():
    #revisa si la carpeta esta o no
    crear_directorio()

    #Mostrar menu de opciones
    mostrar_menu()

    #Preguntar al usuario la accion a utilizar
    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opcion\r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            print('Hasta Luego')
            preguntar = False
        else:
            print('Opcion no valida intente de nuevo')


def mostrar_menu():
    print('Seleccione del Menu lo que deseas hacer:\r')
    print('1) Agregar Contacto\r')
    print('2) Editar Contacto\r')
    print('3) Ver Contacto\r')
    print('4) Buscar Contacto\r')
    print('5) Eliminar Contacto\r')
    print('6) Salir\r')


def agregar_contacto():
    
    print('Escribe los numero del nuevo contacto:\n\r')
    nombre_contacto = input('Nombre del Contacto:\n\r')

    #revisar sie le archivo existe
    existe = existe_contacto(nombre_contacto)

    if not existe:
        telefono_contacto = input('Telefono del Contacto:\n\r')
        categoria_contacto = input('Categoria del Contacto:\n\r')

        #Instanciar Clase
        contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

        #Open y escritura del txt
        with open(CARPETA + contacto.get_nombre() + EXTENSION,'w') as archivo:
            archivo.write(f'Nombre: {contacto.get_nombre()}\r')
            archivo.write(f'Telefono: {contacto.get_telefono()}\r')
            archivo.write(f'Categoria: {contacto.get_categoria()}\r')
        
        print('Se ha guardado exitosamente\r\n')
    else:
        print('Ese Contacto ya existe\r\n')

    app()


#Editar contacto existente
def editar_contacto():
    nombre_editar = input('Escribe el nombre del contacto que quieres editar:\r\n')
    existe = existe_contacto(nombre_editar)

    if existe:

        with open(CARPETA + nombre_editar + EXTENSION,'w') as archivo:

            nombre_contacto = input('Agrega el nuevo nombre:\n\r')
            telefono_contacto = input('Agrega el nuevo telefono:\n\r')
            categoria_contacto = input('Agrega la nueva categoria:\n\r')

            contacto_editado = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            archivo.write(f'Nombre: {contacto_editado.get_nombre()}\r')
            archivo.write(f'Telefono: {contacto_editado.get_telefono()}\r')
            archivo.write(f'Categoria: {contacto_editado.get_categoria()}\r')

        #para renombrar usamos el rename y primero pones la ruta anteiror y despues la actual (con el nombre que queramos) ojo para renombrar tiene que ser despues de with si lo pones dentro tendra errores        
        os.rename(CARPETA + nombre_editar + EXTENSION,CARPETA + nombre_contacto + EXTENSION)
        print('\r\nSe ha Editado exitosamente\r\n')
    else:
        print('no puedes')

    app()


def mostrar_contactos():
    #para listar los archivo utilizamos la funcion listdir(nombre de la carpeta) de os
    archivos = os.listdir(CARPETA)

    #para listar los los archivos txt la primera i es el iterador
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    #recorremos el array donde estan los archivos txt
    for archivo in archivos:
        #abrimos los archivo txt
        with open(CARPETA + archivo) as contacto:
            #recorremos cada una de las lineas
            for linea in contacto:
                print(linea.rstrip() + '\r\n')

    app()


#buscar un contacto
def buscar_contacto():
    nombre_buscar = input('Seleccione el nombre a buscar:\n\r')
   
    #utilizando try otra forma de hacerlo
    try:
        with open(CARPETA + nombre_buscar + EXTENSION) as contacto:
            for linea in contacto:
                print(linea.rstrip() + '\n\r')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    app()


#Eliminar contacto
def eliminar_contacto():
    nombre_buscar = input('Seleccione el contacto a eliminar:\n\r')

    try:
        os.remove(CARPETA + nombre_buscar + EXTENSION)
        print('Contacto eliminado exitosamente')
    except IOError:
        print('No existe ese contacto')
    
    app()


#Creacion de la carpeta
def crear_directorio():
    if not os.path.exists(CARPETA):
        #creamos la carpeta
        os.makedirs(CARPETA)


#Existe contacto
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()