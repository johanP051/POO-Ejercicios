#Crea una clase Alumno con atributos privados (__nombre, __notas) y métodos públicos (agregar_nota(), promedio(), mejor_nota()). Asegúrate de que las notas estén entre 0 y 10.

class Alumno:
    def __init__ (self,nombre):
        self.__nombre = nombre
        self.__notas = []

    def agregar_nota(self,nota):
        if nota >=0 and nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota fuera de rango")

    def promedio(self):
        return sum(self.__notas)/len(self.__notas)
    
    def mejor_nota(self):
        return max(self.__notas)
    
    def get_nombre(self):
        return self.__nombre
    
def pedir_datos():
    nombre = input("Ingrese el nombre del alumno: ")
    alumno = Alumno(nombre)
    
    cantidad = int(input("Ingrese la cantidad de notas que desea agregar: "))
    
    for i in range (0,cantidad):
        nota = float(input("Ingrese la nota: "))
        alumno.agregar_nota(nota)
    return alumno


def main():
    alumno = pedir_datos()
    print(f"El promedio del alumno {alumno.get_nombre()} es: {alumno.promedio()}")
    print(f"La mejor nota del alumno {alumno.get_nombre()} es: {alumno.mejor_nota()}")

if __name__ == "__main__":
    main()