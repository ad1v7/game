from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def clickable(widget):
    '''
    Allow widget to call function on click

    usage: clickable(widget).connect(function)
    '''
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


def centre_window(MainWindow):
    '''
    Position window in the middle of the active screen
    '''
    frameGm = MainWindow.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    MainWindow.move(frameGm.topLeft())
