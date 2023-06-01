def bodega():
    dicc={}
    f=open('inventario.xlsx','rt')
    matriz=f.readlines() 
    f.seek(0)
    print(len(matriz))
    for i in range (len(matriz)):
        lista=f.readline().rstrip('\n').split(',')
        for j in range(len(lista)):
            pos=str(f'{i}{j}')
            dicc[pos]=lista[j]
    f.close()
    return dicc
if __name__=="__main__":
    bodega()