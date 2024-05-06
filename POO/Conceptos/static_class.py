class MiClase:
    atribut_de_clase = 7

    def __init__(self,color):
        self._color = color
    
    #Una funcion estatico es una funcion que le pertenecera a la clase, ya no se relacionara con instancias que salgan de esta clase
    @staticmethod
    def metodo_statico(color):
        print(f"Este es un metodo estatico puedo interactuar con atributos de objeto {color}")

    #A comparacion de un metodo estatico, este pedira la clase donde proveera este metodo        
    @classmethod
    def metodo_de_clase(cls):
        print(f"Este es un metodo de clase\nPuedo interactuar con los atributos de mi clase {cls.atribut_de_clase}")

miClase = MiClase("Yellow")

MiClase.metodo_statico("Yellow")