import os

class Reproductor():
    def __init__(self, tipo_reproduccion):
        self.tipo_reproduccion = tipo_reproduccion
    def reproducir(self):
        print(f"\nRecuerde que el archivo {self.tipo_reproduccion} debe estar en la carpeta 'media'")
        pathDF = "/media/sebas/Exdrive/PROGRAMACION\ II/trabajoClase/tallerPOO/Polimorfismo/media/"
        path = input("\nInserte el path del vídeo, deje vacío para dejar el path por defecto: ")
        if path == "":
            path = pathDF

        archivo = input("\nInserte el nombre del archivo (incluya el formato) : ")
        print("\nAbriendo el archivo ...")
        path = os.path.join(path, archivo)
        
        
        try:
            os.system("xdg-open " + path)
        except Exception as e:
            print(f"\n\nError: {e}")

class ReproductorMP3(Reproductor):
    def __init__(self, tipo_reproduccion):
        super().__init__(tipo_reproduccion)

    def decorador_mp3(funcion):
        def funcionReproducir_modificada(self):
            print("Descargando datos del servidor de Youtube ...")
            funcion(self)
            print("Datos descargados satisfactoriamente")
            print("Reproduciiendo el vídeo ...")
        return funcionReproducir_modificada

    @decorador_mp3
    def reproducir(self):
        return super().reproducir()
    
class ReproductorStreaming(Reproductor):
    def __init__(self, tipo_reproduccion):
        super().__init__(tipo_reproduccion)

    def decorador_Streaming(funcion):
        def funcionReproducir_modificada(self):
            print("Asegúrese de que tenga una buena conexión a internet")
            print("Conexión establecida con el servidor")
            funcion(self)
            print("Los datos se están descargando del servidor a medida que se reproduce en vivo")
            print("Reproduciendo el vídeo ...")
        return funcionReproducir_modificada
    
    @decorador_Streaming
    def reproducir(self):
        return super().reproducir()


opciones = {
    1: "Reproducir MP3",
    2: "Reproducir Streaming"
}


def reproducir_tipo(clase, tipo_reproduccion_):
    rep = eval(clase)(tipo_reproduccion_)
    return rep


while True:
    try:
        opcion = int(input(f"Seleccione la opción {opciones}: "))
    except Exception as e:
        print(e)
    if opcion not in opciones.keys():
        print("\nSeleccione una opcion válida:\n")
        print(opciones)
    else:
        break

match opcion:
    case 1:
        rep = reproducir_tipo("ReproductorMP3", "mp3")
        rep.reproducir()
    case 2:
        rep = reproducir_tipo("ReproductorStreaming", "mp4")
        rep.reproducir()
        

    

