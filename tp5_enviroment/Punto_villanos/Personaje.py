import re
from typing import Tuple
from data_structures import ProbeHashMap

class Personaje():
    def __init__(self, nombre, bando):
        self.nombre = nombre
        self.bando = bando

    def __repr__(self):
        return f"{self.bando}: {self.nombre}"

    @staticmethod
    def leer_archivo(archivo):
        with open(archivo, 'r') as f:
            return f.readlines()

    @staticmethod
    def clasificar_personajes(lineas):
        personajes = []
        patron = r'(?P<bando>super_heroe|villano)\((?P<nombre>[a-z_]+(?:_[a-z_]+)*)\)'
        for linea in lineas:
            linea = linea.strip()
            coincidencia = re.match(patron, linea)
            if coincidencia:
                bando = coincidencia.group('bando').replace("_" , " ")
                nombre = coincidencia.group('nombre').replace("_", " ")
                personajes.append(Personaje(nombre, bando))
        
        return personajes
    
    @staticmethod
    def contar_superheroes_y_villanos():
        archivo = 'superheroes_villanos.txt'
        mapa = ProbeHashMap()

        mapa["superheroe"] = 0
        mapa["villano"] = 0
        
        with open(archivo, 'r') as f:
            for linea in f:
                if linea.startswith("super_heroe"):
                    mapa["superheroe"] += 1
                elif linea.startswith("villano"):
                    mapa["villano"] += 1
        
        return mapa["superheroe"], mapa["villano"]
