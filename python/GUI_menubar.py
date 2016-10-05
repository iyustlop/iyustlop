from PyQt4 import QtGui,QtCore
import sys

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window,self).__init__()
		self.initUI();

	def initUI(self):
		exitAction = QtGui.QAction(QtGui.QIcon('studio.png'), '&Exit'		
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("PyQt")
		self.setWindowIcon(QtGui.QIcon('studio.png'))		
		
		extractAction =  QtGui.QAction("get",self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip('Leave the App')
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		btn = QtGui.QPushButton("Quit",self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())
		btn.move(100,100)
		self.show()

	def close_application(self):
		print("cosas")
		sys.exit()

		
app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())




