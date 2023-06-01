class Articulos():
    def __init__(self):
        self.__idArticulo=None
        self.__precioBase=None
        self.__unidExistencia=None

    def setidArticulo(self,id:int):
        self.__idArticulo=id
    
    def setPrecioBase(self,precio:float):
        self.__precioBase=precio
    
    def setUnidExistente(self,unidad:int):
        self.__unidExistencia=unidad

    def getIdArticulo(self):
        return self.__idArticulo
    
    def getPrecioBase(self):
        return self.__precioBase
    
    def getUnidExistente(self):
        return self.__unidExistencia  

class Licores(Articulos):
    def __init__(self):
        super().__init__()
        self.__precio=None
        self.__presentacion=None
        self.__numero=None

    
    def setPrecio(self,precio:int):
        self.__precio=precio
    
    def setPresentacion(self,presentacion:str):
        self.__presentacion=presentacion

    def setNumero(self,numero:int):
        self.__numero=numero

    def getPrecio(self):
        return self.__precio
    
    def getPresentacion(self):
        return self.__presentacion
    
    def getNumero(self):
        return self.__numero

class Galletas(Articulos):
    def __init__(self):
        super().__init__()
        self.__precio=None
        self.__presentacion=None
        self.__numero=None

    def setPrecio(self,precio:int):
        self.__precio=precio
    
    def setPresentacion(self,presentacion:str):
        self.__presentacion=presentacion

    def setNumero(self,numero:int):
        self.__numero=numero

    def getPrecio(self):
        return self.__precio
    
    def getPresentacion(self):
        return self.__presentacion
    
    def getNumero(self):
        return self.__numero

class Dulces(Articulos):
    def __init__(self):
        super().__init__()
        self.__precio=None
        self.__presentacion=None
        self.__numero=None

    
    def setPrecio(self,precio:int):
        self.__precio=precio
    
    def setPresentacion(self,presentacion:str):
        self.__presentacion=presentacion

    def setNumero(self,numero:int):
        self.__numero=numero

    def getPrecio(self):
        return self.__precio
    
    def getPresentacion(self):
        return self.__presentacion
    
    def getNumero(self):
        return self.__numero

class Helados(Articulos):
    def __init__(self):
        super().__init__()
        self.__precio=None
        self.__presentacion=None
        self.__numero=None

    
    def setPrecio(self,precio:int):
        self.__precio=precio
    
    def setPresentacion(self,presentacion:str):
        self.__presentacion=presentacion

    def setNumero(self,numero:int):
        self.__numero=numero

    def getPrecio(self):
        return self.__precio
    
    def getPresentacion(self):
        return self.__presentacion
    
    def getNumero(self):
        return self.__numero


def lectura():
    n = open('inventario.xlsx','rt')
    data = [[],[],[]]
    linea = n.readline().rstrip('\n').split(',')
    while linea != ['']:
        if linea[3]=='AGUARDIENTE':
            obj=Licores()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5]))
            obj.setUnidExistente(int(linea[7]))
            obj.setPresentacion(linea[3])
            obj.setNumero(int(linea[2]))
            data[0].append(obj)
        elif linea[3]=='GALLETAS':
            obj=Galletas()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5]))
            obj.setUnidExistente(int(linea[7]))
            obj.setPresentacion(linea[3])
            obj.setNumero(int(linea[2]))
            data[1].append(obj)
        elif linea[3]=='DULCES':
            obj=Dulces()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5]))
            obj.setUnidExistente(int(linea[7]))
            obj.setPresentacion(linea[3])
            obj.setNumero(int(linea[2]))
            data[2].append(obj)
        elif linea[3]=='HELADOS':
            obj=Helados()
            obj.setidArticulo(int(linea[0]))
            obj.setPrecioBase(float(linea[5]))
            obj.setUnidExistente(int(linea[7]))
            obj.setPresentacion(linea[3])
            obj.setNumero(int(linea[2]))
            data[3].append(obj)
        linea = n.readline().rstrip('\n').split(',')
    n.close()
    return data

def com():
    data=lectura()
if __name__=="__main__":
    com()