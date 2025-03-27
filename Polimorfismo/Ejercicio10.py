#Define una clase Notificacion con un método enviar(mensaje). Luego, crea subclases como Email, SMS y PushNotification que implementen enviar() de forma distinta según el canal.

class Notificacion:
    def enviar(self,mensaje):
        pass

class Email(Notificacion):
    def enviar(self,mensaje):
        print(f"Email recibido: {mensaje}")

class SMS(Notificacion):
    def enviar(self,mensaje):
        print(f"Tienes un SMS nuevo2: {mensaje}")

class PushNotification(Notificacion):
    def enviar(self,mensaje):
        print(f"Tienes una push notification: {mensaje}")

def pedir_mensaje():
    mensaje = input("Ingrese el mensaje: ")
    return mensaje

def main():
    
    print("Opciones de mesnaje:")
    print("1. Email")
    print("2. SMS")
    print("3. PushNotification")
    
    opcion = int(input("Ingrese el número correspondiente al canal de notificación deseado: "))

    mensaje = pedir_mensaje()

    match opcion:

        case 1:
            email = Email()
            email.enviar(mensaje)
        case 2:
            sms = SMS()
            sms.enviar(mensaje)
        case 3:
            push = PushNotification()
            push.enviar(mensaje)
        case _:
            print("Opción no existente")
            return

if __name__ == "__main__":
    main()
    