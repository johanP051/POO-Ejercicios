#Crea una clase base Animal con atributos como nombre y edad, y métodos como comer() y dormir(). Luego, define subclases como Perro, Gato y Pájaro que hereden de Animal y añadan métodos específicos (ladrar(), maullar(), volar()).

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        pass

    def dormir(self):
        pass

class Perro(Animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.raza = raza

    def ladrar(self):
        return("Guau")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Raza: {self.raza}, Ladrido: {self.ladrar()}"

class Gato(Animal):
    def __init__(self,nombre,edad,color):
        super().__init__(nombre,edad)
        self.color = color

    def maullar(self):
        return("Miau") 

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Color: {self.color}, Maullido: {self.maullar()}"

    
class Pajaro(Animal):
    def __init__(self,nombre,edad,tamanio):
        super().__init__(nombre,edad)
        self.tamanio = tamanio

    def volar(self):
        return("Puede volar")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tamaño: {self.tamanio}, Habilidad: {self.volar()}"

        
def pedir_datos_perro():
    nombre = input("Ingrese el nombre del perro: ")
    edad = input("Ingrese la edad del perro: ")
    raza = input("Ingrese la raza del perro: ")
    return Perro(nombre, edad, raza)

def pedir_datos_gato():
    nombre = input("Ingrese el nombre del gato: ")
    edad = input("Ingrese la edad del gato: ")
    color = input("Ingrese el color del gato: ")
    return Gato(nombre, edad, color)

def pedir_datos_pajaro():
    nombre = input("Ingrese el nombre del pájaro: ")
    edad = input("Ingrese la edad del pájaro: ")
    tamanio = input("Ingrese el tamaño del pájaro: ")
    return Pajaro(nombre, edad, tamanio)

def main():
    print("Lista de animales:")
    print("1. Perro")
    print("2. Gato")
    print("3. Pájaro")

    opcion = int(input("Ingrese el número correpondiente al animal deseado: "))	

    match opcion:
        case 1:
            animal = pedir_datos_perro()
        case 2:
            animal = pedir_datos_gato()
        case 3:
            animal = pedir_datos_pajaro()
        case _:
            print("Opción no existente")
            return

    print(animal)

if __name__ == "__main__":
    main()

