# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 21:05:58 2016

@author: portatil
"""

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFileDialog

class Directoy_Button(QtGui.QWidget):
    
        def __init__(self):
            super(Directoy_Button,self).__init__()
            
            self.initUI()
           
        def initUI(self):
            self.setGeometry(300,300,250,150)
            self.setWindowTitle('Objetivo: Ejecutar Macro')
            
            qbtn = QtGui.QPushButton('Quit', self)
            qbtn.clicked.connect(self.set_Directory())
            qbtn.resize(qbtn.sizeHint())
            qbtn.move(50, 50)               
            
            self.showMaximized()
                        
        def set_Directory(self):
            self.__directorio = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            #self.__directorio = 'directorio destino'
        
        def get_Directory(self):
            return self.__directorio
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    boton_directorio = Directoy_Button()
    print (boton_directorio.get_Directory())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  

           



                
            