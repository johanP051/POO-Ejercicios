#Define una clase Empleado con atributos como nombre, salario y método calcular_bono(). Luego, crea subclases como Gerente, Desarrollador y Asistente que hereden de Empleado y modifiquen el cálculo del bono según su rol.

class Empleado():
    def __init__(self,nombre,salario,ventas):
        self.nombre = nombre
        self.salario = salario
        self.ventas = ventas

    def calcular_bono(self):
        pass

class Gerente(Empleado):
    def __init__(self,nombre,salario,ventas):
        super().__init__(nombre,salario,ventas)

    def calcular_bono(self):
        if self.ventas >= 50 :
            return self.salario * 0.5
        else:
            return print (0)

class Desarrollador(Empleado):
    def __init__(self,nombre,salario,ventas):
        super().__init__(nombre,salario,ventas)

    def calcular_bono(self):
        if self.ventas >= 50 :
            return self.salario * 0.3
        else:
            return print (0)

class Asistente(Empleado):
    def __init__(self,nombre,salario,ventas):
        super().__init__(nombre,salario,ventas)

    def calcular_bono(self):
        if self.ventas >= 50 :
            return self.salario * 0.1
        else:
            return print (0)
        
def pedir_datos_gerente():
    nombre = input("Ingrese el nombre del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    ventas = int(input("Ingrese la cantidad de ventas: "))
    return Gerente(nombre,salario,ventas)

def pedir_datos_desarrollador():
    nombre = input("Ingrese el nombre del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    ventas = int(input("Ingrese la cantidad de ventas: "))
    return Desarrollador(nombre,salario,ventas)

def pedir_datos_asistente():
    nombre = input("Ingrese el nombre del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    ventas = int(input("Ingrese la cantidad de ventas: "))
    return Asistente(nombre,salario,ventas)

def main():
    print("Lista de empleados:")
    print("1. Gerente")
    print("2. Desarrollador")
    print("3. Asistente")
    opcion = int(input("Ingrese el número correspondiente al empleado deseado: "))

    match opcion:
        case 1:
            empleado = pedir_datos_gerente()
        case 2:
            empleado = pedir_datos_desarrollador()
        case 3:
            empleado = pedir_datos_asistente()
        case _:
            print("Opción no existente")
            return
        
    print(f"El bono del empleado {empleado.nombre} es: {empleado.calcular_bono()}")
        
if __name__ == "__main__":
    main()
