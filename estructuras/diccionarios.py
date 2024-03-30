#Diccionarios = Objeto JSON
usuarios = {
    "nombre": "John",
    "apellido":"Doe",
    "edad": 20,
    "colores": ["Rojo","Verde","Azul"],
    #Se pueden agregar diccionarios dentro de otros
    "dictionary": {
        "key":"value1",
        "key2":"value2"
    }
}
#print(usuarios["colores"])
#De ambas maneras es valido para crear un diccionario
jugador = dict(equipo="X",salario=3000,equipos=["1","2","3"])
print(usuarios["dictionary"])