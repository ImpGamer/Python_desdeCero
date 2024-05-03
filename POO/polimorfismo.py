class Shape:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y,radius):
        super().__init__(x, y,width=1,height=1)
        self.radius = radius

    def draw(self):
        print(f"Imprimiendo la forma de un circulo {self.x}, {self.y} y su radio es: {self.radius}")

class Triangle(Shape):
    def __init__(self, x, y,base,altura):
        super().__init__(x, y, altura, base)
        self.altura = altura
        self.base = base
    def draw(self):
        print(f"Imprimiendo un triangulo en {self.x}, {self.y} con una base {self.base} y altura {self.altura}")

class Rectangule(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self):
        print(f"Imprimiendo un rectangulo con sus medidas: \nAncho: {self.width}\nAlto: {self.height}")

circulo = Circle(x=100,y=50,radius=25)
triangulo = Triangle(x=100,y=100,base=20,altura=150)
rectangulo = Rectangule(x=100,y=20,width=100,height=50)

circulo.draw()
triangulo.draw()
rectangulo.draw()