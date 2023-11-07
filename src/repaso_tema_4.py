from collections import namedtuple
import csv
from datetime import datetime

Libro = namedtuple("Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")


def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


# TODO: Implemente las funciones solicitadas en el enunciado
def libro_mas_reciente(libros, autor):
    pass

def libro_titulo_mas_corto(libros, autor = None):
    pass

def libros_mas_caros(libros, año=None):
    pass

def ordena_libros_por_año_y_autor(libros):
    pass


if __name__ == "__main__":
    libros = lee_libros("data/libreria.csv")
    print(f"Se han leído {len(libros)} libros.")

    print("\nLibro más reciente de Gabriel García Márquez:", libro_mas_reciente(libros, "Gabriel García Márquez"))
    print("===================================")

    print("El libro con el título más corto de todos es:", libro_titulo_mas_corto(libros))
    print("El libro con el título más corto de todos es de Gabriel García Márquez:", libro_titulo_mas_corto(libros, "Gabriel García Márquez"))
    print("===================================")

    print("Los libros más caros de todos son:")
    for libro in libros_mas_caros(libros):
        print("\t", libro)
    print("\nLos libros más caros del año 1985 son:")
    for libro in libros_mas_caros(libros, 1985):
        print("\t", libro)
    print("===================================")

    print("Los libros ordenados por año, y a igualdad de año, por autor:")
    for libro in ordena_libros_por_año_y_autor(libros):
        print("\t", libro)