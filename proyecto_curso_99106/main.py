import sys
import PyQt5.QtWidgets as PyQT
from inv import inve as v
from PyQt5 import uic
from categoria import cat as c

class principal(PyQT.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initGui1()
        self.initGui2()
        self.initGui3()
        self.initGui4()
        self.initGui5()
        self.initGui6()
        self.initGui7()
        self.initGui8()
        self.initGui9()

    def initGui1(self):
        uic.loadUi('inicio_de_sesion.ui',self)
        self.show()
        self.inicio.clicked.connect(self.inicio.currentChanged.connect(self.self.initGui2()))
    
    def initGui2(self):
        uic.loadUi('inicio.ui',self)
        self.show()
        self.inicio.clicked.connect(lambda: self.ingresar())
        
    
    def initGui3(self):
        uic.loadUi('principal_adm.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.adm())
    
    def initGui4(self):
        uic.loadUi('principalclien.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.clien())
    
    def initGui5(self):
        uic.loadUi('pedido.ui',self)
        self.show()
        self.final.clicked.connect(self.pedido.currentChanged.connect(self.self.initGui7()))

    def initGui6(self):
        uic.loadUi('inventario.ui',self)
        self.show()
        self.aceptar.clicked.connect(lambda: self.inv())

    def initGui7(self):
        uic.loadUi('factura.ui',self)
        self.show()
        self.finalizar.clicked.connect(lambda: self.ingresar())

    def initGui8(self):
        uic.loadUi('deudas.ui',self)
        self.show()
        self.inicio.clicked.connect(lambda: self.ingresar())

    def initGui9(self):
        uic.loadUi('comidadisp.ui',self)
        self.show()

    def ingresar(self):
        tex=self.usuario.text()
        texto=self.con.text()
        comprobar=True
        while comprobar:
            if tex=='adm123' and texto=='suport123':
                comprobar=False
                self.ingresar.clicked.connect(self.inicio_de_sesion.currentChanged.connect(self.self.initGui3()))
            elif tex=='cliente123' and texto=='123456':
                comprobar=False
                self.ingresar.clicked.connect(self.inicio_de_sesion.currentChanged.connect(self.self.initGui4()))
            else:
                comprobar=True
    def adm(self):
        if self.inventario.isChecked()==True:
            self.aceptar.clicked.connect(self.principal_adm.currentChanged.connect(self.self.initGui6()))
        elif self.deudas.isChecked()==True:
             self.aceptar.clicked.connect(self.principal_adm.currentChanged.connect(self.self.initGui8()))

    def inv(self):
        if self.inventario.isChecked()==True:
            self.resultado.setText(str(v))
        elif self.bodega.isChecked()==True:
            self.resultado.setText(str(b))
    def clien(self):
        if self.comidadisp.isChecked()==True:
            self.aceptar.clicked.connect(self.principalclien.currentChanged.connect(self.self.initGui5()))
        elif self.pedido.isChecked()==True:
             self.aceptar.clicked.connect(self.principalclien.currentChanged.connect(self.self.initGui8()))
    def comida(self):
        if self.inventario.isChecked()==True:
            self.mostrar.setText(str(c))
        elif self.bodega.isChecked()==True:
            self.mostrar.setText(str(c))    
        elif self.inventario.isChecked()==True:
            self.mostrar.setText(str(c))
        elif self.bodega.isChecked()==True:
            self.mostrar.setText(str(c))


        


def main():
    app = PyQT.QApplication([])
    window = principal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()