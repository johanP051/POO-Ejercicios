#Crea una clase base Figura con métodos area() y perimetro(). Luego, implementa subclases como Circulo, Rectangulo y Triangulo que hereden de Figura y calculen sus áreas y perímetros según sus atributos.
import numpy as np

class Figura:
    def __init__(self):
        self.area = 0
        self.perimetro = 0 

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self,radio):
        super().__init__()
        self.radio = radio
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        self.area = np.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        self.perimetro = 2 * np.pi * self.radio

    def __str__(self):
        return f"Radio del círculo: {self.radio} Área: {self.area:.4f}, Perímetro: {self.perimetro:.4f}"

class Triangulo(Figura):
    def __init__(self,base,altura,lado1,lado2,lado3):
        super().__init__()   
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        self.area = (self.base * self.altura)/2

    def calcular_perimetro(self):
        self.perimetro = self.lado1 + self.lado2 + self.lado3

    def __str__(self):
        return f"Base : {self.base}, Altura : {self.altura}, Área: {self.area:.4f}, perimetro: {self.perimetro:.4f}"
    
class Rectangulo(Figura):
    def __init__(self,base,altura):
        super().__init__()
        self.base = base
        self.altura = altura
        self.calcular_area()
        self.calcular_perimetro()

    def calcular_area(self):
        self.area = self.altura * self.base 

    def calcular_perimetro(self):
        self.perimetro = (self.altura * 2) + (self.base * 2)
        
    def __str__(self):
        return f"Base : {self.base}, Altura : {self.altura}, Área: {self.area:.4f}, perimetro: {self.perimetro:.4f}"

def pedir_datos_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    return Circulo(radio)

def pedir_datos_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    lado1 = float(input("Ingrese el lado 1 del triángulo: "))
    lado2 = float(input("Ingrese el lado 2 del triángulo: "))
    lado3 = float(input("Ingrese el lado 3 del triángulo: "))
    return Triangulo(base,altura,lado1,lado2,lado3)

def pedir_datos_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    return Rectangulo(base,altura)

def main():
    print("Lista de números correspondientes a las figuras:")
    print("1. Círculo")
    print("2. Triángulo")
    print("3. Rectángulo")

    opcion = int(input("Ingrese el número correpondiente a la figura deseada: "))	

    match opcion:
        case 1:
            figura = pedir_datos_circulo()
        case 2:
            figura = pedir_datos_triangulo()
        case 3:
            figura = pedir_datos_rectangulo()
        case _:
            print("Opción no existente")
            return


    print(figura)

if __name__ == "__main__":
    main()

    