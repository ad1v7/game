from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from game.utils import clickable

try:
    _fromUtf8 = lambda s: s
except AttributeError:
    def _fromUtf8(s):
        return s

class Soldier_icon_(QWidget):
    '''
    Soldier() widget used in Roster or BT view
    '''
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.gridLayoutWidget = QWidget()
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 131, 93))
        self.gridLayoutWidget.setFixedSize(131,93)
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QTableWidget(self.gridLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(122, 50))
        self.tableWidget.setMaximumSize(QSize(125, 50))
        self.tableWidget.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(61)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(15)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.titleBar = QWidget(self.gridLayoutWidget)
        self.titleBar.setMinimumSize(QSize(125, 25))
        self.titleBar.setMaximumSize(QSize(125, 20))
        self.titleBar.setStyleSheet(_fromUtf8("background-color: lightgrey"))
        self.titleBar.setObjectName(_fromUtf8("titleBar"))
        self.vlLayout = QHBoxLayout(self.titleBar)
        self.vlLayout.setContentsMargins(-1, -1, -1, 4)
        self.vlLayout.setSpacing(3)
        self.vlLayout.setObjectName(_fromUtf8("vlLayout"))
        self.Unit_name = QLabel(self.titleBar)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Unit_name.setFont(font)
        self.Unit_name.setStyleSheet(_fromUtf8(""))
        self.Unit_name.setObjectName(_fromUtf8("Unit_name"))
        self.vlLayout.addWidget(self.Unit_name)
        self.in_battle_squad_chbx = QCheckBox(self.titleBar)
        self.in_battle_squad_chbx.setMinimumSize(QSize(18, 16))
        self.in_battle_squad_chbx.setMaximumSize(QSize(18, 16))
        self.in_battle_squad_chbx.setText(_fromUtf8(""))
        self.in_battle_squad_chbx.setObjectName(_fromUtf8("in_battle_squad_chbx"))
        self.vlLayout.addWidget(self.in_battle_squad_chbx)
        self.remove_unit = QPushButton(self.titleBar)
        self.remove_unit.setMinimumSize(QSize(16, 16))
        self.remove_unit.setMaximumSize(QSize(16, 16))
        self.remove_unit.setObjectName(_fromUtf8("remove_unit"))
        self.vlLayout.addWidget(self.remove_unit)
        self.gridLayout.addWidget(self.titleBar, 1, 0, 1, 1)
        self.health_bar_2 = QProgressBar(self.gridLayoutWidget)
        self.health_bar_2.setMinimumSize(QSize(80, 4))
        self.health_bar_2.setMaximumSize(QSize(120, 4))
        self.health_bar_2.setStyleSheet("::chunk { background-color: red}")
        self.health_bar_2.setTextVisible(False)
        self.health_bar_2.setOrientation(Qt.Horizontal)
        self.health_bar_2.setObjectName(_fromUtf8("health_bar_2"))
        self.gridLayout.addWidget(self.health_bar_2, 2, 0, 1, 1)
        self.setLayout(self.gridLayout)

    def retranslate_widget(self, squad, soldier, rm_func, update_func, expand):
        '''
        Fill widget with Soldier() data

        squad: squad soldier belongs to
        soldier: units.Soldier() object
        rm_func: delete unit function assigned to 'x' button
        update_func: update function which refreshes current view
        expand: function called when widget is clicked to show unit 
                expanded view
        '''
        item = self.tableWidget.item(0, 0)
        item.setText("MO: %s" % soldier.morale)
        item = self.tableWidget.item(0, 1)
        item.setText(u"\xA3%s" % soldier.cost)
        item = self.tableWidget.item(1, 0)
        item.setText("MV: %s" % soldier.move)
        item = self.tableWidget.item(1, 1)
        item.setText("AR: %s" % soldier.armour)
        item = self.tableWidget.item(2, 0)
        item.setText("SH: %s" % soldier.shoot)
        item = self.tableWidget.item(2, 1)
        item.setText("FT: %s" % soldier.fight)
        self.Unit_name.setText("%s" % soldier.name)
        self.remove_unit.setText("x")
        self.remove_unit.clicked.connect(lambda: rm_func(self, squad, soldier))
        self.in_battle_squad_chbx.stateChanged.connect(lambda: update_func())
        clickable(self).connect(lambda: expand(soldier))
        self.health_bar_2.setProperty("value", soldier.health)
        self.tableWidget.itemClicked.connect(lambda: expand(soldier))
