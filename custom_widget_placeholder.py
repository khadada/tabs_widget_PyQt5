# Import necessary classes:
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor

# Create custom widget of Qwidget class:
class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        # Switch on background fill
        self.setAutoFillBackground(True)
        # Create wrap 
        palette = self.palette()
        # Set color to the wrap
        palette.setColor(QPalette.Window, QColor(color))
        # Set the palette to this custom QWidget class:
        self.setPalette(palette)