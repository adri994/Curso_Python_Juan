#GETTER y SETTER

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


#instancia clase

restaurant = Restaurant('Pizza Adrian','Comida Italiana',1000)
restaurant.get_precio()
restaurant.set_precio(80)
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Pizza Ana','Comida Española',2000)
restaurant2.mostrar_informacion()