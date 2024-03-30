edad = int(input("Ingrese su edad: "))
EDAD_BASE = 18

if edad > EDAD_BASE:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 anos de edad") 
else:
    print("Eres menor de edad")