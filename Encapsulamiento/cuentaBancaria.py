from sys import exit

class CuentaBancaria():
    def __init__(self, saldo, titular):
        self.__saldo = saldo
        self.__titular = titular 

    @property
    def saldo(self):
        print(f"\n{self.__titular}, su saldo actual es de: {self.__saldo}\n")
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo
        return self.__saldo

    @property
    def titular(self):
        print(f"\nEl titular de la cuenta es: {self.__titular}\n")
    
    @saldo.setter
    def saldo(self, nuevo_titular):
        self.__titular = nuevo_titular
        return self.__titular

    def depositar(self, deposito_dinero):
        self.__saldo += deposito_dinero
        print(f"\nSe ha depositado {deposito_dinero}. El nuevo saldo es de {self.__saldo}\n")

    def retirar(self):
        while True:
            try:
                retiro_dinero = float(input(f"\n{self.__titular}, inserte el valor del monto del retiro: "))
            except Exception as e:
                print(f"\nError: {e}\n")
                continue
            if retiro_dinero > self.__saldo:
                print(f"\nNo puede retirar una cantidad mayor al saldo actual.\n")
                print(f"{self.__titular}, su saldo actual es de: {self.__saldo}, y está tratando de retirar {retiro_dinero}\n")
                continue
            else:
                self.__saldo -= retiro_dinero
                print(f"\nHa retirado {retiro_dinero}.\nEl nuevo saldo es de {self.__saldo}\n")
                break


def ejecucion():
    while True:
        titular_1 = input("\nInserte el titular de la cuenta: ")
        saldo_1 = float(input(f"\nIngrese el saldo inicial del usuario {titular_1}: "))
        cuenta = CuentaBancaria(saldo_1, titular_1)
        
        while True:
            print("\nOpciones:")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir\n")
            opcion = int(input(f"{titular_1}, seleccione una opción: "))


            match opcion:
                case 1:
                    cuenta.saldo
                case 2:
                    deposito_dinero_1 = float(input(f"\n{titular_1}, inserte el valor del monto del depósito: "))
                    cuenta.depositar(deposito_dinero_1)
                case 3:
                    cuenta.retirar()
                case 4:
                    print("\nSaliendo del programa ...\n")
                    exit(0)
                case _:
                    print("\nOpción no válida.\n")
            
            cambio_usuario = input(f"\n¿Desea cambiar de usuario? (S/n): ")
            if cambio_usuario.lower() == "s":
                break
                    

if __name__ == "__main__":
    ejecucion()