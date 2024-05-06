class Usuario:
    def __init__(self,apellido,nombre,contraseina):
        #Creacion de atributos publicos
        self._nombre = nombre
        self._apellido = apellido
        self._contraseina = contraseina

    #Getter
    @property
    def nombre(self):
        return self._nombre
    #Setter
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
        
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido    

usuario1 = Usuario(apellido="Romero",nombre="David",contraseina="12345")
print(usuario1.nombre)
print(usuario1.apellido)