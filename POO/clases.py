#Creacion de una clase para generar objetos a partir de esta
#Una buena practica es nombrar el nombre del archivo como la clase
class Usuario(): #Nombre de la clase
    #Atributos de la clase:
    def __init__(self,nombre,apellido,correo,password,telefono): #Creacion del metodo constructor
        #La palabra "self" sirve similar a la palabra reservada "this" de otros lenguajes
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.telefono = telefono

#Metodos de la clase
    #Si algun metodo de la clase no requiere parametros hay que poner la palabra reservada "self"
    def encriptPassword(self):
        return "Encriptando..."
    def verifyPassword(self):
        return "Verificando password..."
    def toString(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nTelefono: {self.telefono}"


usuario1 = Usuario(
    nombre="David",
    apellido="Rodriguez",
    correo="David990@gmail.com",
    password="123450",
    telefono="18239184"
)
print(usuario1.toString())