#Herencia

class Restaurant:

    def __init__(self,nombre,categoria,precio): #esto es un constructor
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio

 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
    
    #GETTER y SETTER GET = obtinee un valor y set =modifica valor

    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio=precio

#Crear clase hijo de Restaurant
class Hotel(Restaurant):#asi se hereda
    def __init__(self,nombre,categoria,precio):
        super().__init__(nombre,categoria,precio)

hotel = Hotel('Casa Sammy','Cinco Estrella',200)
hotel.mostrar_informacion()