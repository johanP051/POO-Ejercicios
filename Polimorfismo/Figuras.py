from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np

class Figura(ABC):
    @abstractmethod
    def dibujar(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def dibujar(self):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.radio * np.cos(theta)
        y = self.radio * np.sin(theta)
        plt.plot(x, y)
        plt.title(f"Círculo con radio {self.radio}")
        plt.axis("equal")
        plt.show()

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        x = [0, self.lado, self.lado, 0, 0]
        y = [0, 0, self.lado, self.lado, 0]
        plt.plot(x, y)
        plt.title(f"Cuadrado con lado {self.lado}")
        plt.axis("equal")
        plt.show()

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def dibujar(self):
        x = [0, self.base, self.base / 2, 0]
        y = [0, 0, self.altura, 0]
        plt.plot(x, y)
        plt.title(f"Triángulo con base {self.base} y altura {self.altura}")
        plt.axis("equal")
        plt.show()

if __name__ == "__main__":
    print("Elige una figura para dibujar:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Triángulo")
    opcion = int(input("Introduce el número de la figura: "))
    
match opcion:
    case 1:
        radio = float(input("Introduce el radio del círculo: "))
        figura = Circulo(radio)
    case 2:
        lado = float(input("Introduce el lado del cuadrado: "))
        figura = Cuadrado(lado)
    case 3:
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        figura = Triangulo(base, altura)
    case _:
        print("Opción no válida.")
        exit()

figura.dibujar()