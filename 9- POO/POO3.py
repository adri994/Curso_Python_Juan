#Encapsulamiento

class Restaurant:

    def __init__(self,nombre,categoria,precio): #esto es un constructor
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio #default Public, Protected se representa con un_ y puede modificar en toda la clase
        #__ es para ponerlo en private
 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

#instancia clase

restaurant = Restaurant('Pizza Adrian','Comida Italiana',1000)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Pizza Ana','Comida Española',2000)
restaurant2.mostrar_informacion()