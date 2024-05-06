#El metodo super() permite realizar la funcionalidad completa de la clase padre, a aquella que este heredando
class Mascota:
    a = None

    def __init__(self,nombre):
        self._nombre = nombre

    def jugar(self):
        print(f"La mascota {self._nombre} esta jugando!")
    
class Perro(Mascota):
    def __init__(self,nombre,raza,edad):
        super().__init__(nombre)
        self._raza = raza
        self._edad = edad
    
    def jugar(self):
        super().jugar()
        print(f"De raza {self._raza} con su hueso!")

perro = Perro(nombre="Sally",raza="Fox Terrrier",edad=12)