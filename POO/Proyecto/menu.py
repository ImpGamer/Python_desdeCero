class MainMenu:

    @staticmethod
    def showMainMenu():
        print("**************************")
        print("Agenda de contacto")
        print("***************************")
        print(
            "1.Agregar Contacto\n2.Listar Contactos\n3.Buscar Contacto\n4.Editar Contacto\n5.Cerrar aplicacion"
        )
    
    @staticmethod
    def showMenuAddContact():
        print("***************************")
        print("Agregar Nuevo Contacto")
        print("***************************")
    @staticmethod
    def showContactsMenu():
        print("***************************")
        print("Mis contactos guardados")
        print("***************************")
        print("Nombre   |   Telefono    |   Correo")

    @staticmethod
    def showFindContact():
        print("\n****************************************************")
        print("PRESIONA 1 para SALIR")
        phone = input("Ingrese el telefono del contacto que desea buscar: ")
        return phone
    
    @staticmethod
    def showEditContact(contacto):
        print("\n*********************************")
        print(f"Editar contacto: '{contacto.nombre}'")
        print("***********************************")
