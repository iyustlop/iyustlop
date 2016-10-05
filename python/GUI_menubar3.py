import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Captor_E Repositioner Perfomance analysis')    
        self.setWindowIcon(QtGui.QIcon('studio.png'))
        
        extractAction = QtGui.QAction("&Exit", self)        
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Exit application')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        self.home()
        
    def home(self):
        print("Accesing to home")
	
	# Creacion del boton de salida               
        btn = QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        #btn.resize(btn.minimumSizeHint())
        btn.move(0,70)
	
	#crea la barra de estatus
        self.statusBar()

	# Creo las acciones que van en el toolbar.
        # Son Abrir fichero y Cerrar la aplicacion
        openAction = QtGui.QAction(QtGui.QIcon('ic_folder_open_black_36dp.png'),'Open file',self)
        openAction.triggered.connect(self.open_file)

        extractAction = QtGui.QAction(QtGui.QIcon('ic_exit_to_app_black_18dp.png'),'Quit application',self)
        extractAction.triggered.connect(self.close_application)
	
        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(extractAction)
        
        checkBox = QtGui.QCheckBox('Enlarge windows',self)
        checkBox.move(0,250)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        #Progress Bar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download",self)
        self.btn.move(0,40)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())	
        self.styleChoice = QtGui.QLabel("Windows Vista",self)

        comBox = QtGui.QComboBox(self)
        comBox.addItem("motif")
        comBox.addItem("Windows")
        comBox.addItem("cde")
        comBox.addItem("Plastique")
        comBox.addItem("Cleanlooks")
        comBox.addItem("windowsvista")

        comBox.move(50,250)
        self.styleChoice.move(50,150)
        comBox.activated[str].connect(self.style_choice)

 	# Inicia la aplicacion maximizada
        self.showMaximized()       

    def style_choice(self, text):
        self.stykeChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    # Agranda la ventana.
    def enlarge_window(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,600)

    def download(self):
        self.completed = 0
            
        while self.completed < 100:
                self.completed += 0.001
                self.progress.setValue(self.completed)

    #Abre el fichero csv
    def open_file(self):
        print("Open")

    #cierra la aplicacion
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Salir',"¿Desea salir?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

