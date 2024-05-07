from contacts import Contacto
from menu import MainMenu

misContactos = []

def mostrarMenu():
    option = 0

    while option != 5:
        MainMenu.showMainMenu()
        option = int(input("Ingrese la opcion que desea realizar: "))
        if option < 1 or option >5:
            print("Opcion invalida. Intente de nuevo")
        else:
            realizarAccion(option)
    print("Fin del programa, gracias por usar :D")

def realizarAccion(option):
    match option:
        case 1:
            agregarNuevoContacto()
        case 2:
            mostrarContactos()
        case 3:
            buscarContacto()
        case 4:
            editarContacto()


def agregarNuevoContacto():
    MainMenu.showMenuAddContact()
    name = input("Ingrese el nombre del contacto: ")
    phone = input("Ingrese el numero del contacto: ")
    entrada_email = input("Ingrese email del usuario (Opcional): ")

    email = entrada_email if entrada_email != "" else "No posee"
    contacto = Contacto(
        nombre=name,
        telefono=phone,
        email=email
    )
    misContactos.append(contacto)

def mostrarContactos():
    if len(misContactos) == 0:
        print("No hay contactos registrados\n")
        return False
    MainMenu.showContactsMenu()
    for index,contact in enumerate(misContactos,start=1):
        print(f"{index}. {contact.nombre}\t{contact.telefono}\t{contact.email}")
    return True

def buscarContacto():
    phone = 0

    while int(phone) != 1:
        contactoEnc = None

        phone = MainMenu.showFindContact()
        if len(phone) != 10:
            print("El telefono que se ingreso no es valido. Intente de nuevo")      
        else:
            for contact in misContactos:
                if contact.telefono == phone:
                    contactoEnc = contact
                    break
            if contactoEnc != None:
                print(f"\nContacto encontrado!")
                MainMenu.showContactsMenu()
                print(f"{contactoEnc.nombre}\t{contactoEnc.telefono}\t{contactoEnc.email}")

            else:
                print(f"No se encontró ningún contacto con el teléfono: {phone}")
def editarContacto():
    if mostrarContactos():
       contactIndex = int(input("Ingresa el numero del contacto que desees editar: "))
       try:
        MainMenu.showEditContact(misContactos[contactIndex-1])
        contactoEditar = misContactos[contactIndex-1]

        contactoEditar.nombre = input("Ingrese el nuevo nombre: ")
        contactoEditar.telefono = input("Ingrese el nuevo telefono: ")
        entrada_email = input("Ingrese el nuevo email (Opcional): ")

        email = entrada_email if entrada_email != "" else "No posee"
        contactoEditar.email = email

        misContactos[contactIndex-1] = contactoEditar
        print("Contacto editado correctamente!")
       except IndexError:
           print("El numero ingresado no es valido.")

mostrarMenu()