from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from game.units import Soldier

try:
    _fromUtf8 = lambda s: s
except AttributeError:
    def _fromUtf8(s):
        return s

class Add_Unit_Button(QWidget):
    '''
    Button Widget used in Roster and BT view

    func(value) is called when clicked

    '''
    def __init__(self, func, value, parent=None):
        super(Add_Unit_Button, self).__init__(parent)
        gridLayoutWidget = QWidget()
        gridLayoutWidget.setGeometry(QRect(0,0, 131, 93))
        gridLayoutWidget.setMinimumSize(QSize(131, 93))
        gridLayout = QGridLayout(gridLayoutWidget)
        self.add_unit_button = QPushButton()
        self.add_unit_button.setFixedSize(55, 55)
        self.add_unit_button.setStyleSheet(_fromUtf8("background-color: yellow;\n"
                                                "color: black;" "font-size:10pt;"))
        def function():
            func(value)

        self.add_unit_button.setText("Buy\nUnit")
        self.add_unit_button.clicked.connect(lambda: function())
        gridLayout.addWidget(self.add_unit_button)
        self.setLayout(gridLayout)

    def set_text(self, text):
        self.add_unit_button.setText(text)

    '''
    def eventFilter(self, object, event):
        if event.type() == QEvent.HoverMove:
            self.add_unit_button.setStyleSheet("background-color:#45b545;")
            print("C'mon! CLick-meeee!!!")
            return True
        #elif event.type() == QEvent.MouseButtonPress:
        #    print('clicked')
        #    return True
        return False
    '''

    def enterEvent(self, event):
        self.add_unit_button.setStyleSheet("background-color:green;")

    def leaveEvent(self,event):
        self.add_unit_button.setStyleSheet("background-color:yellow;")


class PopupWindow(QMainWindow):
    '''
    Popup with grid layout and vertical scrollbar when needed

    self.layout: add widgets here
    '''
    def __init__(self, parent=None):
        super(PopupWindow, self).__init__(parent)
        self.centralWidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralWidget)
        self.scrollArea = QScrollArea(self.centralWidget)
        self.layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 580, 460))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.layout = QGridLayout(self.scrollAreaWidgetContents)
        self.layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.layout.setContentsMargins(0, 0, 0, 20)
        self.setCentralWidget(self.centralWidget)
