class Restaurant:

    def agregar_restaurant(self,nombre): #siempre hay que poner self para que funcione ya que es lo que utilizamos para leer los atributos
        self.nombre = nombre
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')


#Instanciar clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizza Adrian')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Pizza Ana')
restaurant2.mostrar_informacion()

#Otra forma de mostrar los datos
print(f'Nombre: {restaurant.nombre}')
print(f'Nombre: {restaurant2.nombre}')