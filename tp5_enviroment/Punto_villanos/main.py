from Personaje import Personaje
class Ejecutable:
    @staticmethod
    def main():
        archivo = 'c:\\Users\\GAMER\\tp5_2\\tp5_prueba\\tp5_enviroment\\Punto_villanos\\superheroes_villanos.txt'
        lineas = Personaje.leer_archivo(archivo)
        personajes = Personaje.clasificar_personajes(lineas)
        for personaje in personajes:
            print(personaje)

        cantidad_superheroes, cantidad_villanos = Personaje.contar_superheroes_y_villanos()
        print(f"Cantidad de superheroes: {cantidad_superheroes}")
        print(f"Cantidad de villanos: {cantidad_villanos}")

if __name__ == "__main__":
    Ejecutable.main()
