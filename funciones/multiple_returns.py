#Dentro de python y varios lenguajes de programacion, una funcion es capaz de devolver 1 valor, ningun valor o multiples valores, en esta seccion
# nos adentraremos y mostraremos el retorno de multiples valores mediante una sola funcion

#Retorno de un solo valor
def suma(number1,number2):
    return number1+number2;

#Retorno de muchos valores
def operaciones_matematicas(num1,num2):
    suma = num1+num2
    resta = num1-num2
    multiplicacion = num1*num2
    division = num1/num2
    return suma,resta,multiplicacion,division

#Impresion de los datos a la funcion print(), que devolvera en forma de tupla
print(operaciones_matematicas(20,30))

#De acuerdo al orden especificado dentro de la funcion, y las variables declaradas para recibir esos datos, se almacenaran dentro de las variables en ese mismo orden
suma,resta,multiplicacion,division = operaciones_matematicas(30,140)

#Solamente imprimimos la variable "suma" que recibimos de la funcion "operaciones_matematicas"
print("La suma es: "+str(suma))