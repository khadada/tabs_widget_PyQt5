# import necessary class and modules:
from re import S
import sys
from PyQt5.QtWidgets import(QApplication,QMainWindow,QWidget,QTabWidget)
from custom_widget_placeholder import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
        
    def initialize_ui(self):
        """
        Initalize the main window then display its content
        """
        self.setWindowTitle("Tab_")
        self.setGeometry(40, 40, 600, 800)
        self.display_content()
    
    def display_content(self):
        """
        Display widgets of the main screen window
        """
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        for n , color in enumerate(["red","blue","green","yellow"]):
            tabs.addTab(Color(color),color)
        
        self.setCentralWidget(tabs)

# Run program:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tab_app = MainWindow()
    sys.exit(app.exec_())
        