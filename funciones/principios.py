# Una funcion, es una porcion de codigo especifica a una accion, donde se puede llamar y ejecutar la cantidad de veces que sea necesario
# Palabra reservada "def" para declarar funciones
def fibonacci(n):
    a,b = 0,1
    while a<n:
        print(a, end=" ")
        a,b = b, a+b
    print()

#Invocamos a nuestra funcion, al devolver un String podemos almacenarlo en una variable o directamente imprimirlo
#serie = fibonacci() #me devuelve el String y lo guardo dentro de la variable
#print(fibonacci()) #O se imprime directamente sin necesidad de guardarlo en ningun lugar

#Oh en  el caso que no nos retorne nada podemos declarar la funcion inmediatamente
fibonacci(20)
fibonacci(2000)
"""
Parametros y Argumentos:
Un parametro es un dato que pedira la funcion para funcionar de manera correcta, ya sea especificado o de otro dato que la funcion necesite para realizar su accion,
Un argumento es aquel dato que al momento de declarar la funcion le enviaremos
"""