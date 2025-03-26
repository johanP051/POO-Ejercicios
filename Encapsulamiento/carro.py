class Carro():
    def __init__(self, marca: str, modelo: str, ano: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    def get_info(self):
        print(f"Este coche es marca: {self.__marca}, modelo: {self.__modelo} y año: {self.__ano}")
        
    def set_modelo(self):
        while True:
            try:
                nuevo_modelo = input("Modifique el modelo del carro: ")
            except Exception as e:
                print(e)
                continue
            if nuevo_modelo.rstrip() == "":
                print("El modelo está vacío, inserte un modelo valido")
                continue
            else:
                self.__modelo = nuevo_modelo
                break
                
            

def ejecucion():
    while True:
        print("\n--- Registro de Carro ---")
        
        try:
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            ano = int(input("Año: "))
            break
        except Exception as e:
            print(e)

            
        mi_carro = Carro(marca, modelo, ano)
        
        while True:
            print("\nOpciones:")
            print("1. Ver información del carro")
            print("2. Modificar modelo del carro")
            print("3. Registrar otro carro")
            print("4. Salir\n")
            
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("\nOpción inválida. Debe ingresar un número.\n")
                continue

            match opcion:
                case 1:
                    mi_carro.get_info()
                case 2:
                    mi_carro.set_modelo()
                case 3:
                    print("\nRegistrando otro carro...\n")
                    break
                case 4:
                    print("\nSaliendo del programa...\n")
                    exit(0)
                case _:
                    print("\nOpción no válida.\n")


if __name__ == "__main__":
    ejecucion()