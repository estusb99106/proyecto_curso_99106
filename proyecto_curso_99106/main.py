import sys
import PyQt5.QtWidgets as PyQT
from inv import inve as v
from bodega import bodega as b
from PyQt5 import uic
from factura import fac as f
from comida import com as c
from busqueda import bus as bu

class principal(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui1()
    def initGui1(self):
        uic.loadUi('inicio_de_sesion.ui',self)
        self.show()
        self.inicio.clicked.connect(self.ingreso)
    def ingreso(self):
        self.ingreso=segunda()
        self.inicio.show()    
class segunda(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui2()
    def initGui2(self):
        uic.loadUi('inicio.ui',self)
        self.show()
        self.ingresar.clicked.connect(lambda:self.Ingreso())
    def Ingreso(self):
        tex1=self.usuario.text()
        texto2=self.con.text()
        if tex1=='adm' and texto2=='suport':
                self.Ingreso=tercero()
                self.ingresar.show()   
        elif tex1=='cliente' and texto2=='clien':
                self.Ingreso=cuarto()
                self.ingresar.show()         
class tercero(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui3()     
    def initGui3(self):
        uic.loadUi('principal_adm.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.adm())
    def adm(self):
        if self.inventario.isChecked()==True:
            self.adm=sexto()
            self.aceptar.show()   
        elif self.deudas.isChecked()==True:
            self.adm=octavo()
            self.aceptar.show()
class cuarto(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui4()
    def initGui4(self):
        uic.loadUi('principalclien.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.clien())
    def clien(self):
        if self.comidadisp.isChecked()==True:
            self.clien=noveno()
            self.aceptar.show()
        elif self.pedido.isChecked()==True:
            self.clien=quinto()
            self.aceptar.show()
class quinto(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui5()
    def initGui5(self):
        uic.loadUi('pedido.ui',self)
        self.show()
        self.finalizar.clicked.connect(lambda:self.facturar())
    def facturar(self):
        self.facturar=septimo()
        self.factura.show()
class sexto(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui6()
    def initGui6(self):
        uic.loadUi('inventario.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.inv())
    def inv(self):
        if self.inventario.isChecked()==True:
            self.inven2.setText(str(v))
        elif self.bodega.isChecked()==True:
            self.bod.setText(str(b))
class septimo(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui7()
    def initGui7(self):
        uic.loadUi('factura.ui',self)
        self.show()
        self.mostrar.clicked.connect(lambda: self.fa())
    def fa():
        self.factura.setText(str(bu))
class octavo(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui8()
    def initGui8(self):
        uic.loadUi('deudas.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda:self.deu())
    def deu(self):
        if self.debe.isChecked()==True:
            self.debe2.setText(str(v))
        elif self.fiado.isChecked()==True:
            self.fiado2.setText(str(b))   
class noveno(PyQT.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui9()
    def initGui9(self):
        uic.loadUi('comidadisp.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.comida())
    def comida(self):
        if self.dulces.isChecked()==True:
            self.mostrar.setText(str(c))
        elif self.helados.isChecked()==True:
            self.mostrar.setText(str(c))    
        elif self.galletas.isChecked()==True:
            self.mostrar.setText(str(c))
        elif self.licores.isChecked()==True:
            self.mostrar.setText(str(c))
def main():
    app = PyQT.QApplication([])
    window = principal()
    window.show
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()