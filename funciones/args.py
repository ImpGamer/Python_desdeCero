#Si una funcion requiere de muchos parametros para funcionar, se usara la siguiente sintaxis:

#De esta manera le decimos, que la cantidad de parametros que puede recibir es ilimitado
def func(*args):
    for item in args:
        print(item)

#Le podemos enviar la cantidad de argumentos que desemos
func(2,"Azul","Rusia",True,-30)

"""
Realmente esto no es muy utilizado o considerado como una buena practica, a menos que nuestra funcion si se adapte a cualquier tipo de dato y cantidad
de parametros recibidos, pero si no, esto puede llegar a ser un gran problema
"""

#Si deseamos enviar un tipo de dato especifico como un diccionario, tupla o lista, lo
#haremos con "kargs" como parametro

days = { #Declaracion de diccionario
    "dia1":"Lunes",
    "dia2":"Martes",
    "dia3":"Miercoles",
    "dia4":"Jueves"
}

def dictionary(**kargs):
    print(kargs)

#Le estamos especificando que "days" no es una variable comun, si no que se trata de un tipo de dato
dictionary(**days)