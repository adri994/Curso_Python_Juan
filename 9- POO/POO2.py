#Abstraccion y Constructores

class Restaurant:

    def __init__(self,nombre,categoria,precio): #esto es un constructor
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
 
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

#instancia clase

restaurant = Restaurant('Pizza Adrian','Comida Italiana',1000)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Pizza Ana','Comida Española',2000)
restaurant2.mostrar_informacion()

