class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Guau"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau"

class Vaca(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Muu"

if __name__ == "__main__":
    nombre = input("Introduce el nombre del animal: ")
    tipo = input("Introduce el tipo de animal (Perro, Gato, Vaca): ")

    if tipo.lower() == "perro":
        animal = Perro(nombre)
    elif tipo.lower() == "gato":
        animal = Gato(nombre)
    elif tipo.lower() == "vaca":
        animal = Vaca(nombre)
    else:
        print("Tipo de animal no reconocido.")
        exit()

    print(animal.hablar())