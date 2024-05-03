from cryptocode import encrypt, decrypt
from abc import ABC, abstractclassmethod

#Definicion de una clase abstracta o padre
#Una clase abstracta o padre es aquella que tendra atributos y metodos pero no tendra logica, es decir solo
#sirve para que se creen otras clases hijas a partir de esta, heredando metodos y atributos
class UsuarioBase(ABC):
    def __init__(self,nombre,apellido,correo,contraseina,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseina = self.encriptarContraseina(contraseina)
        self.telfono = telefono

    @abstractclassmethod    
    def encriptarContraseina(self,contraseina):
        pass

    @abstractclassmethod
    def verificarContraseina(self,contraseina):
        pass

class UsuarioConcreto(UsuarioBase):
    
    def encriptarContraseina(self,contraseina):
        return encrypt(contraseina, "secret")
    
    def verificarContraseina(self,contraseina):
        contraseina_desencriptada = decrypt(self.contraseina,"secret")
        return contraseina_desencriptada == contraseina
    
usuario = UsuarioConcreto(
    nombre="David",
    apellido="Rodriguez",
    correo="miCorreo@gmail.com",
    contraseina="miContraseina123",
    telefono="1029840918"
)

password = input("Ingrese su contrasena para verificarla: ")

if usuario.verificarContraseina(password):
    print("La contraseina ingresada es valida")
else:
    print("La contraseina ingresada no es valida")