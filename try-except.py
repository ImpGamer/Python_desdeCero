"""
El flujo try-except, funciona como un try-catch en los demas lenguajes de programacion, es decir
el bloque "try" intentara realizar esa parte del codigo que es propensa a provocar fallos, y que
tratamos de controlar, en caso que esa parte del codigo si falle, la controlaremos con el bloque
"except" donde el flujo del programa puede parar o tomar otro camino, de esa manera, en caso de errores
por parte de la aplicacion o usuario, no bloquee o pare el programa completo
"""
num = int(input("Ingrese el numero a dividir: "))
div = int(input("Ingrese por el numero que desea dividirlo: "))

try:
    print(num/div)
    #Es recomendable saber que tipo de error estamos controlando, por lo que especifica el bloque "except" que
    #tipo de error debe capturar
except ZeroDivisionError:
    #Bloque de codigo que se ejecutaara en caso que se produzca un error del bloque "try"
    print("Se a producido un error al tratar de realizar la division")
    #Bloque finally que se ejecuta no importa si hubo error o no.
finally: 
    print("El programa sigue...")