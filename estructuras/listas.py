#Lista = Array
frutas = ["Manzana","Uva","Pera","Guayaba","Jamaica","Jicama","Platano"]
varios = [True,"Azul",20,33.33,-300]

#Marcar un rango de un arreglo, es decir de un punto (index) hasta otro y almacenarlo
#En este caso estamos diciendo que en "frutas2" almacenara los valores que se encuentran entre el index 1 y 4 de "frutas"
frutas2 = frutas[1:4] 
#Dentro de python podemos agregar elementos de un array a otro array o lista
numeros = [1,2,3,4]
new_list = varios +numeros

#Darle nuevo valor a un rango
new_list[1:4] = ["Pablo",990,"Numeros",False,"Verde"]
#Funcion lenght para saber longitud de datos
#print(len(new_list))
#Dentro de python podemos almacenar arrays dentro de arrays!
arrays = [new_list,frutas]
#Accedemos al array que se encuentra dentro del array, y ese array interior obtendremos su 3 indice
print(arrays[0][3])
print(arrays[1])