from comida import com as m


def facturar(data):
    carrito=[[],[],[]]
    item=input('Id del Articulo: ')
    while item != 'fin':
        for i in range(3):
            for j in data[i]:
                if (j.getIdArticulo()==int(item)) and (j.getUnidExistente()>0):
                    carrito[i].append(j)
                    j.setUnidExistente(j.getUnidExistente()-1)
                elif (j.getIdArticulo()==int(item)) and (j.getUnidExistente()<=0):
                    print('Existencia insuficiente')

        item=input('Id del Articulo: ')
    return carrito
                

def fac():
    carrito=facturar(m)
    print(carrito)


if __name__=="__main__":
    fac()