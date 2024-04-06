"""
Dentro de las funciones, los parametros pueden variar, dependiendo si se pasa como argumento una variable o un numero establecido, pero le podemos pasar constantes?
es decir que ese parametro requerido, siempre sea el mismo en todos los casos? asi es y lo realizamos de la siguiente manera
"""
#Sin embargo para declarar algo mas constante que si o si no cambie
# lo haremos desde los propios parametros de la funcion
def suma(num1,num2=10):
    print(num1+num2)

#Deseamos que el numero 2 (num2) de parametro siempre sea 10 y "num1" sea una variable por parte del usuario (input)
num1 = int(input("Ingrese un numero: "))

#De esta manera le estamos diciendo a la funcion => que el primer parametro sera la variable tomada, y el segundo parametro ssera el valor tomado por el parametro
suma(num1=num1)