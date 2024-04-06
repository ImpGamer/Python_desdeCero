"""
Dentro de los lenguajes de programacion en general, existe una regla al momento de usar variables o constantes en un archivo y este es llamado como "scope" o alcance
y existen 2 solamente => Global y local.
Global: Declaramos la variable o constante fuera de cualquier funcion, en el archivo principal, de esa manera todo nuestro archivo y funciones tendran acceso a esa
variable, de esta manera podemos evitar repeticion de variables o predifinirlas.
Local: Es una variable o constante declarada dentro de una funcion, el cual solo esa funcion tendra acceso directo, podremos utilizarlo en otras partes pero tendra que ser
pasado como argumento.
Ya dependera de que funcionalidad le aplicaras a esa variable o constante para considerar si declararlo global o local.
Ahora veremos como funciona esto dentro de python
"""
#Como no se encuentra dentro de ningun bloque de codigo o funcion, es declarada de manera global (todo el archivo tiene acceso a ella)
name = "Kevin"

def func():
    #Deseamos imprimir la variable "name" sin embargo existen 2!, cual imprimira? debido al scope, la funcion le tomara mas importancia o se percatara primero de las variables
    # locales, esto quiere decir que imprimira la variable local antes que la global
    """
    Sin embargo que sucede si yo deseo utilizar mi variable global dentro de mi funcion, pero una variable local ya posee ese nombre, como le puedo decir al interprete
    de python que deseo utilizar la variable global y no la local
    """
    #Uso de la variable global
    global name
    # declaracion de una nueva variable local "name" que usara la variable global "name" y "Hola!"
    name = name + "Hola!"
    print(name)

func()