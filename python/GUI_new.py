import sys
import numpy as np
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        # Pongo el titulo y el icono de la ventana.
        self.setWindowTitle('Captor_E Repositioner Perfomance analysis')    
        self.setWindowIcon(QtGui.QIcon('studio.png'))

        # llamo creo el menu principal
        self.madeMainMenu()

        # llamo creo la status Bar
        self.madeStatusBar()

        # llamo creo la status Bar
        self.home()

        # Lo inicio maximizado.
        self.showMaximized()

    # funcion menu principal
    def madeMainMenu(self):

        def accionDeSalir():
            # Creo la accion de salir.
            extractAction = QtGui.QAction(QtGui.QIcon('ic_exit_to_app_black_36dp'),"&Exit", self)  
            extractAction.setShortcut("Ctrl+Q")
            extractAction.setStatusTip('Exit application')
            extractAction.triggered.connect(self.close_application)

            return extractAction

        def accionDeAbrir():
            # Creo la accion de abrir un fichero
            openAction = QtGui.QAction(QtGui.QIcon('ic_folder_open_black_36dp.png'),'&Open file',self)
            openAction.setShortcut("Ctrl+O")
            openAction.setStatusTip('Open file')
            openAction.triggered.connect(self.open_file)

            return openAction

        mainMenu = self.menuBar()        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(accionDeAbrir())
        fileMenu.addAction(accionDeSalir())

        toolBar = self.addToolBar("ToolBar")
        toolBar.addAction(accionDeAbrir())
        toolBar.addAction(accionDeSalir())

    def madeStatusBar(self):
	#crea la barra de estatus
        statusBar = self.statusBar()

    #Abre el fichero csv
    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self,'Open File')

        print(name)
        TIME,AESA_DEMAND,BULK_DEMAND,AESA_Current_Position_PRM,Bulk_Current_Position_PRM,AESA_Current_Position_EST,Bulk_Current_Position_EST,AESA_Current_Velocity_EST,Bulk_Current_Velocity_EST,AESA_Integral_Control,Bulk_Integral_Control,AESA_Disturbance_EST,Bulk_Disturbance_EST,AESA_Torque,Bulk_Torque,AESA_Control_Mode,Bulk_Control_Mode,MSG_Counter,MDU_Status,FIN = np.genfromtxt(name,delimiter=';',skiprows=1,autostrip=True,unpack=True)

    #cierra la aplicacion
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Salir',"¿Desea salir?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    # funcion menu principal
    def home(self):
        print("ac")

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

main()
