#La herencia es un pilar de POO, el cual a partir de una clase puede crear mas con diferentes capacidades sin dejar de lado
#los metodos y atributos de la clase padre
#Clase base donde se pueden crear muchos vehiculos
class Vehiculo():
    def __init__(self,marca,modelo,velocidad,año):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.año= año

    def acelerar(self,aceleracion):
        self.velocidad += aceleracion
        return f"La nueva velocidad es: {self.velocidad}"
    
    def desacelerar(self,desaceleracion):
        self.velocidad -= desaceleracion
        return f"La nueva velocidad es: {self.velocidad}"
    def toString(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nVelocidad: {self.velocidad}\nAño: {self.año}"
#Esta nueva clase heredara de la clase vehiculo agregando sus metodos y atributos a esta nueva clase "Motocicleta"
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad, año, motor):
        #La palabra "super" se refiere a que usara el metodo de la clase padre pasando los atributos que necesita
        super().__init__(marca, modelo, velocidad, año)
        #Se le agrega un nuevo atributo solo para esta clase "Motocicleta"
        self.motor = motor

    #Metodo solo para la clase "Motocicleta"    
    def realizarTruco(self,truco):
        return f"Se esta realizando el truco: '{truco}'"
    def toString(self):
        return super().toString()+f"\nMotor: {self.motor}"
    
class Autobus(Vehiculo):
    def __init__(self, marca, modelo, velocidad, año,asientos,pasajeros):
        super().__init__(marca, modelo, velocidad, año)
        self.asientos = asientos
        self.pasajeros = pasajeros

    def subirPasajeros(self,nuevosPasajeros):
        self.pasajeros += nuevosPasajeros
        return f"Pasajeros actuales: {self.pasajeros}"
    
    def bajarPasajeros(self,pasajerosSalir):
        self.pasajeros -= pasajerosSalir
        return f"Pasajeros actuales: {self.pasajeros}"
    def toString(self):
        return super().toString()+f"\nAsientos: {self.asientos}\nPasajeros actuales: {self.pasajeros}"
    
#Una vez creada nuestras 3 clases podemos instanciar elementos de ellas
motocicleta = Motocicleta("Honda",2022,120,2023,"De 4 cilindros")
print(motocicleta.realizarTruco("caballito"))

autobus = Autobus(
    marca="Toyota",
    modelo=2021,
    velocidad=100,
    año=2022,
    asientos=50,
    pasajeros=15
)
print(autobus.toString())