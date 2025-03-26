import random

class Personaje:
    def __init__(self, nombre, vida=100):
        self.nombre = nombre
        self.vida = vida

    def atacar(self):
        return 5

class Guerrero(Personaje):
    def atacar(self):
        return random.randint(15, 20)  
class Mago(Personaje):
    def atacar(self):
        return random.randint(15, 25)  

class Arquero(Personaje):
    def atacar(self):
        return random.randint(8, 22)  

class Criatura:
    def __init__(self, vida=100):
        self.vida = vida

    def atacar(self):
        return random.randint(15, 20)  

def crear_personaje():
    print("Bienvenido al juego. Elige tu personaje:")
    nombre = input("Ingresa el nombre de tu personaje: ")
    print("Elige un rol:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    opcion = int(input("Ingresa el número de tu elección: "))
    
    match opcion:
        case 1:
            return Guerrero(nombre)
        case 2:
            return Mago(nombre)
        case 3:
            return Arquero(nombre)
        case _:
            print("Opción no válida.")
            return crear_personaje()


def juego():
    personaje = crear_personaje()
    criatura = Criatura()

    print(f"\n¡Comienza la batalla entre {personaje.nombre} y la criatura!")
    while personaje.vida > 0 and criatura.vida > 0:
        print(f"\n{personaje.nombre}: {personaje.vida} de vida | Criatura: {criatura.vida} de vida")
        numero_correcto = random.randint(1, 2)
        print("Adivina el número (1 o 2):")
        eleccion = int(input("Tu elección: "))

        if eleccion == numero_correcto:
            daño = personaje.atacar()
            criatura.vida -= daño
            print(f"¡Adivinaste! {personaje.nombre} ataca y causa {daño} puntos de daño a la criatura.")
        else:
            daño = criatura.atacar()
            personaje.vida -= daño
            print(f"Fallaste. La criatura contraataca y te causa {daño} puntos de daño.")

    if personaje.vida > 0:
        print(f"\n¡Felicidades! {personaje.nombre} ha derrotado a la criatura.")
    else:
        print("\nLa criatura te ha derrotado. Fin del juego.")

if __name__ == "__main__":
    juego()