from Personaje import Personaje
class Ejecutable:
    @staticmethod
    def main():
        archivo = 'superheroes_villanos.txt' 
        #Con el nombre del archivo txt solamente se puede ejecutar desde el directorio Punto_Villano y desde la terminal
        #Con la ruta absoluta del archivo se puede ejecutar desde cualquier directorio
        lineas = Personaje.leer_archivo(archivo)
        personajes = Personaje.clasificar_personajes(lineas)
        for personaje in personajes:
            print(personaje)

        cantidad_superheroes, cantidad_villanos = Personaje.contar_superheroes_y_villanos()
        print(f"Cantidad de superheroes: {cantidad_superheroes}")
        print(f"Cantidad de villanos: {cantidad_villanos}")

if __name__ == "__main__":
    Ejecutable.main()
