from factura import fac as f
def precioVenta(obj):
    return obj.precioFinal()

def imprimir(carrito):
    titulos=['Bebidas ....','Condimentos ','Lácteos ....']
    venta=0
    total=0

    print('\n----------------------------------')
    print('-------Super Max Economico -------')
    print('----------------------------------\n')
    print('Categoria   Cantidad    Precio Acu')
    for i in range(3):
        for j in carrito[i]:
            total += precioVenta(j)
            # print(j)
            # x=input('x')
        venta+=total
        print( f'{titulos[i]}.... {len(carrito[i])}...... {total}USD')
        total=0
    print(f'venta total: ........... {round(venta,2)}USD\n')

def bus():
    carrito=f
    imprimir(carrito)


if __name__=="__main__":
    bus()