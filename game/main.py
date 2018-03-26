import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from game.main_ui import Ui_MainWindow
from game import soldier_widget
from game import leaders_widget
from game.units import *
from game.interface_elements import Add_Unit_Button, PopupWindow
from game.expanded_stats import ExpandedSkillsTable
from game.utils import centre_window
import pkg_resources


class GameEngine(QMainWindow):
    def __init__(self, parent=None):
        super(GameEngine, self).__init__(parent)
        # custom widget list
        self.roster_widgets = []
        self.bt_widgets = []
        self.leaders_widgets = []
        self.popup = None
        # initialise interface and its components
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, self.update_all)
        # next we create a player
        self.player = Player('my@email.com',
                                   'secretpassword',
                                   'username')
        # add squad for a player
        self.player.add_new_squad('CapTree',
                                  'HierTree',
                                  'Scotland')
        # add unit button in a bt view
        squad = self.player.list_of_squads[0]
        self.btn_bt = Add_Unit_Button(self.add_unit_to_bt_popup, squad)
        self.btn_bt.set_text('Add\nUnit')
        # buy unit button in a roster view
        self.btn = Add_Unit_Button(self.add, squad)

        # add some soldiers to the roster
        for i in range(7):
            self.add(self.player.list_of_squads[0])

        # keep copy of leaders widgets
        self.init_leaders()
        # initialise tabs
        self.update_all()

    def arrange_roster(self):
        '''
        Rearange in a roster/battle_team lists.

        This method should be called each time unit is added or removed from
        the roster or the battle team

        Method also adds add unit button at the end of the list
        '''
        soldiers_layout = self.ui.soldiers_roster
        #self.clear_layout(soldiers_layout)
        n = len(self.roster_widgets)
        row = 0
        col = 0
        for i in range(1, n+1):
            if i % 3 == 0:
                self.ui.soldiers_roster.addWidget(self.roster_widgets[i-1],
                                                  row, col)
                row += 1
                col = 0
            else:
                self.ui.soldiers_roster.addWidget(self.roster_widgets[i-1],
                                                  row, col)
                col += 1

        # create button for adding new to the player squad
        soldiers_layout.addWidget(self.btn, row, col)

    def arrange_bt(self):
        '''
        BT
        Partial implementation
        '''
        soldiers_layout = self.ui.soldiers_bt
        self.clear_layout(soldiers_layout)
        n = len(self.roster_widgets)
        row = 0
        col = 0
        j = 1
        self.in_bt = [w for w in self.roster_widgets if
                          w.in_battle_squad_chbx.isChecked()]
        #for i in range(1, n+1):
        #    w = self.roster_widgets[i-1]
        #    if w.in_battle_squad_chbx.isChecked():
        for i, item in enumerate(self.in_bt, 1):
            if i % 3 == 0:
                self.ui.soldiers_bt.addWidget(item, row, col)
                row += 1
                col = 0
            else:
                self.ui.soldiers_bt.addWidget(item, row, col)
                col += 1
                i += 1
                # self.ui.soldiers_bt.addWidget(self.roster_widgets[i-1])

        # create button for adding new to the player battle team
        soldiers_layout.addWidget(self.btn_bt, row, col)

    def add_unit_to_bt_popup(self, squad):
        self.popup = PopupWindow(parent=self)
        self.popup.setGeometry(QRect(100, 100, 640, 480))
        self.popup.setFixedSize(640, 480)
        centre_window(self.popup)
        self.arrange_bt_popup()
        self.popup.show()

    def arrange_bt_popup(self):
        l=self.popup.layout
        self.available = [w for w in self.roster_widgets if not
                          w.in_battle_squad_chbx.isChecked()]
        row = 0
        col = 0
        for i, item in enumerate(self.available, 1):
            if i % 4 == 0:
                l.addWidget(item, row, col)
                row += 1
                col = 0
            else:
                l.addWidget(item, row, col)
                col += 1



    def update_all(self):
        '''
        Main update function for a given tab
        '''
        name = self.ui.active_layout.objectName()
        if 'roster' in name:
            self.arrange_roster()
            self.update_leaders(self.ui.leaders_roster)
        elif 'battle_team' in name:
            self.update_leaders(self.ui.leaders_bt)
            self.arrange_bt()
            if self.popup:
                self.arrange_bt_popup()

    def add(self, squad):
        '''
        Add unit to the roster, create widget and update roster view
        '''
        soldier = Soldier()
        squad.add_to_roster(soldier)
        # create unit widget and fill with data
        widget = soldier_widget.Soldier_icon_()
        # add checkbox functionality
        widget.retranslate_widget(squad, soldier, self.remove,
                                  self.update_all, self.expanded_view)
        # keep copy of a widget so we can update easily
        self.roster_widgets.append(widget)
        # rearange roster view
        self.arrange_roster()

    def expanded_view(self, unit):
        exp_skills = ExpandedSkillsTable()
        exp_skills.retranslate_widget(unit)
        if 'roster' in self.ui.active_layout.objectName():
            exp = self.ui.unit_expanded_roster
            pic = self.ui.unit_pic_roster
            itm = self.ui.unit_items_roster
        if 'battle_team' in self.ui.active_layout.objectName():
            exp = self.ui.unit_expanded_bt
            pic = self.ui.unit_pic_bt
            itm = self.ui.unit_items_bt
        self.clear_layout(exp)
        exp.addWidget(exp_skills)
        # set picture
        pic = QLabel(pic)
        pic.setGeometry(0, 0, 181, 181)
        pixmap = QPixmap(unit.pic)
        pic.setPixmap(pixmap.scaled(181, 181))
        pic.show()
        self.arrange_items(unit, itm)

    def arrange_items(self, unit, layout):
        row = 0
        col = 0
        itemlist = unit.weapons + unit.items
        for i in range(1,7):
            try:
                item = itemlist.pop(0).pic
            except IndexError:
                item = unit.item_empty_slot
            pic = QLabel()
            pixmap = QPixmap(item)
            pic.setPixmap(pixmap.scaled(60, 60))
            if i % 2 == 0:
                layout.addWidget(pic, row, col, Qt.AlignTop)
                row += 1
                col = 0
            else:
                layout.addWidget(pic, row, col, Qt.AlignTop)
                col += 1

    def remove(self, btn, squad, soldier):
        squad.remove_from_roster(soldier)
        self.roster_widgets.remove(btn)
        btn.deleteLater()
        if 'roster' in self.ui.active_layout.objectName():
            self.arrange_roster()
        if 'battle_team' in self.ui.active_layout.objectName():
            self.arrange_bt()
            self.arrange_bt_popup()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().setParent(None)
            elif child.layout() is not None:
                self.clear_layout(child.layout())

    def init_leaders(self):
        captain = self.player.list_of_squads[0].captain
        hierophant = self.player.list_of_squads[0].hierophant
        c_wig = leaders_widget.Leader_icon()
        c_wig.retranslate_widget(captain, self.expanded_view)
        h_wig = leaders_widget.Leader_icon()
        h_wig.retranslate_widget(hierophant, self.expanded_view)
        self.leaders_widgets = [c_wig, h_wig]


    def update_leaders(self, layout):
        self.clear_layout(layout)
        layout.addWidget(self.leaders_widgets[0], 0, 0)
        layout.addWidget(self.leaders_widgets[1], 0, 1)

def main():
	app = QApplication(sys.argv)
	myapp = GameEngine()
	myapp.show()
	sys.exit(app.exec_())
    #version = pkg_resources.require("GameII")[0].version


if __name__ == "__main__":
    main()
