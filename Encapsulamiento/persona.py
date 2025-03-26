from sys import exit

class Persona():
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        print(f"Nombre: {self.__nombre}")
    
    def set_edad(self):
        while True:
            try:
                nueva_edad = float(input(f"Inserte la edad (años): "))
            except ValueError:
                print(f"\n Debe ingresar un entero no negativo")
                continue
            if nueva_edad < 0:
                print(f"\n La edad que ha ingresado es negativa, se tomará como positiva")
                self.__edad = -1 * nueva_edad
                break
            else:
                self.__edad = nueva_edad
                break
    
    def get_edad(self):
        print(f"\nEdad: {self.__edad} años\n")
        
    def get_dni(self):
        print(f"\nDNI: {self.__dni}\n")


def ejecucion():
    while True:
        print("\n--- Registro de Persona ---")
        nombre = input("\nInserte el nombre de la persona: ")
        
        try:
            edad = float(input(f"\nInserte la edad de {nombre}: "))
        except ValueError:
            print("\nIngrese un número")
            continue
            
        while True:
            try: 
                dni = input(f"\nInserte el DNI de {nombre}: ")
            except ValueError:
                print("Deber ser un entero")
                continue
            if len(dni) != 10:
                print(f"El DNI debe contener 10 números")
                continue
            else:
                break
        
        persona = Persona(nombre, edad, dni)
        
        while True:
            print("\nOpciones:")
            print("1. Consultar nombre")
            print("2. Consultar edad")
            print("3. Consultar DNI")
            print("4. Modificar edad")
            print("5. Mostrar todos los datos")
            print("6. Salir\n")
            
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("\nOpción inválida. Debe ingresar un número.\n")
                continue

            match opcion:
                case 1:
                    persona.get_nombre()
                case 2:
                    persona.get_edad()
                case 3:
                    persona.get_dni()
                case 4:
                    persona.set_edad()
                case 5:
                    print("\n--- Datos de la persona ---")
                    persona.get_nombre()
                    persona.get_edad()
                    persona.get_dni()
                case 6:
                    print("\nSaliendo del programa...\n")
                    exit(0)
                case _:
                    print("\nOpción no válida.\n")
            
            cambio_persona = input(f"\n¿Desea registrar otra persona? (S/n): ")
            if cambio_persona.lower() == "s":
                break

if __name__ == "__main__":
    ejecucion()