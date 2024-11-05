from Punto_map.sorted_table_map import SortedTableMap

class SortedTableMapClient(SortedTableMap):
    def main():
        map_instance = SortedTableMap()
        map_instance['a'] = 10
        map_instance['c'] = 30
        map_instance['b'] = 20

        print("Prueba getItem de la clave: a ")
        print(map_instance.__getitem__('a'))
        #map_instance.__getitem__('d') #prueba excepcion

        print(map_instance)

        print(f"Por lo tanto tiene {map_instance.__len__()} elementos ")

        print("Cambiando el valor de la clave a: 19")
        map_instance.__setitem__('a', 19)
        print(map_instance)


        print("Agregando la clave 'd' ")
        map_instance.__setitem__('d', 23)
        print(map_instance)

        print("Eliminando clave d")
        map_instance.__delitem__('d')
        print(map_instance)

        print("Claves del map: ")
        claves = map_instance.__iter__()
        for clave in claves:
            print(clave)

        print("Items del map: ")
        items = map_instance.iter_items()
        for item in items:
            print(item)


    if __name__ == "__main__":
        main()