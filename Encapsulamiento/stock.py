class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    def vender(self, cantidad):
        if self.__stock - cantidad < 0:
            print("No hay suficiente stock para realizar la venta.")
        else:
            self.__stock -= cantidad
    def reponer(self, cantidad):
        self.__stock += cantidad
    def get_info(self):
        return f"Nombre: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}"
    
if __name__ == "__main__":

    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    stock = int(input("Introduce el stock del producto: "))
    producto1 = Producto(nombre, precio, stock)
    print(producto1.get_info())


    while True:
        print("\nOpciones:")
        print("1. Vender producto")
        print("2. Reponer producto")
        print("3. Salir")
        opcion = int(input("Ingresa el número de tu elección: "))

        match opcion:
            case 1:
                cantidad = int(input("Introduce la cantidad a vender: "))
                producto1.vender(cantidad)
                print(producto1.get_info())

            case 2:
                cantidad = int(input("Introduce la cantidad a reponer: "))
                producto1.reponer(cantidad)
                print(producto1.get_info())

            case 3:
                print("Fin del programa.")
                break

            case _:
                print("Opción no válida.")
                break