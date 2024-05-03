class Usuario:
    def __init__(self,apellido,nombre,contraseina,correo,telefono):
        #Creacion de atributos publicos
        self.apellido = apellido
        self.nombre = nombre
        self.contraseina = contraseina
        self.correo = correo
        #Atributo privado (Se le agrega "__" al inicio del atributo)
        self.__telefono = telefono

    def encriptarContraseina(self):
        pass

    def verificarContraseina(self,contraseina):
        pass

    #Getter y Setter de un atributo
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,telefono):
        self.__telefono = telefono

usuario1 = Usuario("Alfredo","David","1234","david1234@gmail.com",21229014)

#Tenemos que usar el Getter debido a que el atributo "telefono" es privado, por lo que fuera de esa clase no puede ser usada
print(usuario1.getTelefono())