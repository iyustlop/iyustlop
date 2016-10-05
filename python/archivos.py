# -*- coding utf-8 -*-

import sys
import numpy as np
from os import listdir
from os.path import isfile, join
#from PyQt4.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton, QFileDialog
from PyQt4 import QtGui
from PyQt4.QtGui import QFont


#mypath = "D:\\Repo\\integracion\\Repositioner Tests\\Repo PBIT Test\\SN_0007_R2_2016_06_15\\Nueva carpeta"


class Example(QtGui.QMainWindow):

    def __init__(self):
            super().__init__()

            self.initUI()

    def initUI(self):

        #QToolTip.setFont(QFont('SansSerif',10))

        self.btnLoadDirectory = QtGui.QPushButton('Cargar Directorio',self)
        #self.btnLoadDirectory.resize(self.btnLoadDirectory.sizeHint())
        self.btnLoadDirectory.resize(120,24)
        self.btnLoadDirectory.move(10, 10)
        self.btnLoadDirectory.clicked.connect(self.load_Directory)

        self.btnAPRM_Process = QtGui.QPushButton('Procesar APRM',self)
        #self.btnAPRM_Process.resize(self.btnAPRM_Process.sizeHint())
        self.btnAPRM_Process.resize(120,24)
        self.btnAPRM_Process.move(10, 35)
        self.btnAPRM_Process.clicked.connect(self.APRM_Process)

        self.statusBar().showMessage('Ready')
                
        self.setGeometry(300,300,500,300)
        self.setWindowTitle('Ejecutar Macro')

        self.showMaximized()

    def load_Directory(self):
        # me creo la llamada al dialogo que carga el directorio.
        # consigo un String que es la dirección
        self.mypath = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))

        # Selecciono los archivos que hay dentro del fichero
        onlyfiles = [f for f in listdir(self.mypath) if isfile (join(self.mypath,f))]

        # Quiero un array que solo tenga APRM*.csv
        CSV_files=[]
        self.APRM_CSV_files=[]
        
        for file in onlyfiles:
            if file.endswith('.csv'):
                CSV_files.append(file)

        for file in CSV_files:
            if file.startswith('APRM'):
                self.APRM_CSV_files.append(file)

        self.statusBar().showMessage('Ficheros cargados')
            
    def APRM_Process(self):
        for file in self.APRM_CSV_files:
            archivo = self.mypath+'/'+file
            print (archivo)
            TIME,AESA_DEMAND,BULK_DEMAND, AESA_Current_Position_PRM,Bulk_Current_Position_PRM,AESA_Current_Position_EST,Bulk_Current_Position_EST,	AESA_Current_Velocity_EST,Bulk_Current_Velocity_EST,AESA_Integral_Control,Bulk_Integral_Control,AESA_Disturbance_EST,Bulk_Disturbance_EST,	AESA_Torque,Bulk_Torque,AESA_Control_Mode,Bulk_Control_Mode,MSG_Counter,MDU_Status,FIN = np.genfromtxt(archivo,delimiter=";",skip_header=1,autostrip=True,unpack=True)
            
            print(TIME)
    
        self.statusBar().showMessage('Ficheros Procesados')

    def get_mypath(self):
        return self.mypath

if __name__ == '__main__':

    app = QtGui.QApplication (sys.argv)

    ex = Example()

    sys.exit(app.exec_())
