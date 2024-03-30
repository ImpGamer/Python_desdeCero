#Generar codigo repetitivo de una manera mas controlada o especifica

#for i in range(10):
  #  print(i)

rango = int(input("Ingrese el rango del ciclo:"))
for item in range(rango+1):
    print(item)

#forEach:
lenguajes = ["Python","Java","JavaScript","Csharp","Rust"]
frameworks = ["Django","Flask","FastApi","TensorFlow","Pandas"]

for lenguaje in lenguajes:
    for framework in frameworks:
        print(framework +" "+lenguaje)

