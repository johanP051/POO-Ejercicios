class Huesped:
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__precio_dia = 100000

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def precio_dia(self):
        return self.__precio_dia
    @precio_dia.setter
    def precio_dia(self, nuevo_precio):
        self.__precio_dia = nuevo_precio

    def descuento(self):
        pass

class Huesped_vip(Huesped):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
    def descuento(self):
        noches = int(input("Ingrese cantidad de noches: "))
        descuento = 0.1
        precio = (self.precio_dia * noches) * descuento
        return f"El precio es de {precio}"     

class Huesped_grupo(Huesped):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
    def descuento(self):
        noches = int(input("Ingrese cantidad de noches: "))
        n_personas = int(input("Ingrese cantidad de personas: "))
        descuento_persona = 0.2
        precio = (self.precio_dia * noches) * (descuento_persona * n_personas)
        return f"El precio para el grupo de huepedes {precio}"


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dni = input("Ingrese su DNI: ")
categoria = print("Ingrese su categoría (1: normal, 2: vip, 3: grupo): ")

opcion = int(input("Ingresa el número de tu elección: "))

match opcion:
    case 1:
        huesped_actual = Huesped_vip(nombre, apellido, dni)
    case 2:
        huesped_actual = Huesped_grupo(nombre, apellido, dni)

    case 3:
        huesped_actual = Huesped(nombre, apellido, dni)

    case _:
        print("Opción no válida.")

if __name__ == "__main__":
    print(huesped_actual.descuento())