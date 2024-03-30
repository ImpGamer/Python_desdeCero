"""
---------------------------------------------------------------------------
acciones extras dentro de un ciclo for
continue => Permite saltar a la siguiente posicion
break => Cuando se ejecuta dentro de un bucle, el bucle se rompera y finalizara
else => Ejecucion de un trozo de codigo una vez el ciclo a finalizado
"""
frameworks = ["Flask","Django","FastApi","Pyramid"]

# Palabra reservada "continue"
for frame in frameworks:
    if frame == "Flask":
        print("Existe Flask") 
        #Con continue le estamos diciendo, una vez entrada a esta condicion pasame al siguiente elemento e ignora este actual
        continue
    print(frame)

for frame in frameworks:
    if frame == "Django":
        print("Django se encuentra dentro de la lista")
        break
    print(frame)

#Palabra "else" como parte de un for
for frame in frameworks:
    print(frame)
    #Finalizado el ciclo se ejecuta el else
else:
    print("\nEl ciclo a finalizado")