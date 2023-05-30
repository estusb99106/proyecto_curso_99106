from typing import List

def inve():
    """
        0 codigo
        1 N°
        2 categoria
        3 articulo
        4 presentacion
        5 costo
        6 precio
        7 cantidad
    """

    file = open('inventario.csv', 'r')

    columns = file.readline().replace("\n", "").split(",")

    companies = file.readlines()

    file.close()

    return len(file)

if __name__=="__main__":
    inve()