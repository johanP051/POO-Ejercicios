class metodo_pago:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def pagar(self):
        pass
    
class Tarjeta(metodo_pago):
    def pagar(self):
        print(f"{self.nombre} estás pagando con tarjeta")
class Efectivo(metodo_pago):
    def pagar(self):
        print(f"{self.nombre} estás pagando con efectivo")
class paypal(metodo_pago):
    def pagar(self):
        print(f"{self.nombre} estás pagando con paypal")
        
if __name__ == "__main__":
    nombre = input("Introduce el nombre del que va a pagar: ")
    tipo = input("Introduce el tipo de metodo de pago (Tarjeta, Efectivo, Paypal): ")
    if tipo.lower() == "tarjeta":
        metodo = Tarjeta(nombre, tipo)
    elif tipo.lower() == "efectivo":
        metodo = Efectivo(nombre, tipo)
    elif tipo.lower() == "paypal":
        metodo = paypal(nombre, tipo)
    else:
        print("Tipo de metodo de pago no reconocido.")
        exit()
    metodo.pagar()