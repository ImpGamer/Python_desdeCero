import os
#Dentro de python tenemos que iniciar nuestra funcion principal, es decir aquella funcion que se
#ejecutara al momnto de arrancar el programa
#Funcion para mostrar las opciones al usuario
RED = '\033[91m'
RESET = '\033[0m'
GREEN = '\033[92m'
todoList = []

def showMenuOptions():
    print("""
        Seleccione la opcion que desea realizar:
          1. Crear una tarea
          2. Marcar como realizada una tarea
          3. Borrar tarea
          4. Mostrar todas las tareas
          5. Salir
          """)
#Funcion para mostrar todas las tareas
def showTodoList():
    #Sirve para que la funcion sepa que estamos utilizando la variable global "todoList"
    global todoList
    print("""
************************************
          Lista de tareas actuales:
          """)
    #Lista "todoList" que usamos de manera global
    for work in todoList:
        #Devuelve la posicion (index) del objeto del array o lista
        print(f"{todoList.index(work) + 1}. {work}")
        print("************************************")

#Funcion para agregar una tarea a la todoList
def addWork():
    os.system("cls") #Linux "clear"
    global todoList
    print("\nCrear nueva tarea")
    newWork = input("Ingrese el nombre de la tarea: ")
    if len(newWork) > 3:
        print(GREEN+"La tarea se a agregado correctamente!"+RESET)
        todoList.append(newWork)
        showTodoList()
    else:
        print(f"{RED} El nombre de la tarea es demasiado corto {RESET}")
        addWork()

def updateWork():
    os.system("cls")
    global todoList
    print("Actualizacion de estado de una tarea")
    showTodoList()
    workId = int(input("Ingrese el numero de la tarea que desea marcar como completada: "))
    try:
        work = todoList[workId-1]
        work += f"{GREEN} COMPLETADO {RESET}"
        todoList[workId-1] = work
        print(f"{GREEN} Tarea actualizada! {RESET}")
    except IndexError:
        print(f"{RED} La tarea que marco no esta disponible. Intentelo de nuevo {RESET}")

#Funcion para eliminar una tarea
def deleteWork():
    os.system("cls")
    showTodoList()
    indexWork = int(input("Ingrese el numero de la tarea que desea eliminar: "))
    try:
        work = todoList[indexWork-1]
    except IndexError:
        print(f"{RED} La tarea que desea eliminar no se encuentra. Intentalo de nuevo {RESET}")

    todoList.remove(work)
    print(f"{GREEN} Se a eliminado la tarea correctamente! {RESET}")

#Funcion principal
def main():
    print(".:Bienvenido al TODO LIST en Python :D:.")
    opcion = 0

    while opcion != 5:
        showMenuOptions()
        opcion = int(input("Ingrese el numero de la opcion: "))
        match opcion:
            case 1:
                addWork()
            case 2:
                updateWork()
            case 3:
                deleteWork()
            case 4:
                showTodoList()
            case 5:
                print("\nFin del programa, gracias por usar :D")
            case _:
                print(RED + "Opcion invalida, intentelo de nuevo"+RESET)


if __name__ == "__main__":
    main()