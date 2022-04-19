# import necessary class and modules:
import sys
from PyQt5.QtWidgets import(QApplication,QMainWindow,QWidget,QTabWidget)
from custom_widget_placeholder import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        
    def initialize_ui(self):
        """
        Initalize the main window then display its content
        """
        self.setWindowTitle("Tab_")
        self.setGeometry(40, 40, 600, 800)
        