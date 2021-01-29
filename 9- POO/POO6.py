#Poliforfismo 

class Restaurant:

    def __init__(self,nombre,categoria,precio): #esto es un constructor
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')
    
    #GETTER y SETTER GET = obtinee un valor y set =modifica valor

    def get_precio(self):
        return self.precio
    
    def set_precio(self,precio):
        self.precio=precio

#Crear clase hijo de Restaurant
class Hotel(Restaurant):#asi se hereda
    def __init__(self,nombre,categoria,precio,alberca):
        super().__init__(nombre,categoria,precio)
        self.alberca = alberca

        #Agregar un Metodo que solo exista en hotel
    def get_alberca(self):
        return self.alberca
    
    #Reescribir un metodo(debe llamarse igual)

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')

hotel = Hotel('Casa Sammy','Cinco Estrella',200,True)
hotel.mostrar_informacion()
alberca = hotel.get_alberca()

