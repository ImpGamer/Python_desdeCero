#El valor match es igual a una condicion switch en otros lenguajes match = switch

num = int(input("Ingrese un numero entre 1 y 5: "))
match num:
    case 1:
        print("El numero es 1")
    case 2:
        print("El numero es 2")
    case 3:
        print("El numero es 3")
    case 4:
        print("El numero es 4")
    case 5:
        print("El numero es 5")
    case 6 | 7:
        print("El numero es 6 o 7")
    case _:
        print("El numero no es entre 1 y 5")