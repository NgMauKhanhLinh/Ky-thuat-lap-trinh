import functools
from random import randrange

from PyQt6.QtWidgets import QPushButton

from Chuong2_cautrucdulieu.BT39.ui.MainWindow39 import Ui_MainWindow

class MainWindow39Ext(Ui_MainWindow):
    def __init__(self):
        self.list = []
        self.previous_button = None
        self.select_index = -1

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_Create.clicked.connect(self.xuly_tao_ngaunhien)
        self.pushButton_delete_selected.clicked.connect(self.xuly_xoa_button_dang_chon)
        self.pushButton_add.clicked.connect(self.xuly_add_button)
        self.pushButton_update.clicked.connect(self.xuly_update_button)
        self.pushButton_delete.clicked.connect(self.xuly_xoa_gia_tri_am)
        self.pushButton_AscSort.clicked.connect(self.xuly_sort_asc)
        self.pushButton_DescSort.clicked.connect(self.xuly_sort_desc)
        self.pushButton_Remove.clicked.connect(self.xuly_remove_all)

    def xuly_tao_ngaunhien(self):
        n = int(self.lineEdit_number.text())
        self.list = [randrange(-100, 101) for _ in range(n)]
        self.createRandom()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def createRandom(self):
        self.clearLayout(self.verticalLayout)
        for i in range(len(self.list)):
            x = self.list[i]
            print(x)
            title = f"{x}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(237, 255, 127);")
            self.verticalLayout.addWidget(btn)
            btn.clicked.connect(functools.partial(self.doi_mau_nen, i))

    def doi_mau_nen(self, i):
        sender = self.MainWindow.sender()
        if self.previous_button is not None:  # Reset previous button style
            self.previous_button.setStyleSheet("background-color: rgb(237, 255, 127);")
        sender.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.previous_button = sender
        self.lineEdit_number.setText(sender.text())
        self.select_index = i

    def xuly_xoa_button_dang_chon(self):
        if self.select_index == -1:
            return
        self.list.pop(self.select_index)
        self.select_index = -1
        self.previous_button = None
        self.lineEdit_number.setText("")
        self.createRandom()

    def xuly_add_button(self):
        random_value = randrange(0, 11)
        self.list.append(random_value)
        btn = QPushButton(text=str(random_value))
        btn.setStyleSheet("background-color: rgb(237, 255, 127);")
        self.verticalLayout.addWidget(btn)
        index = len(self.list) - 1
        btn.clicked.connect(functools.partial(self.doi_mau_nen, index))

    def xuly_update_button(self):
        b = int(self.list[self.select_index])
        update = b // 10
        self.list[self.select_index] = update
        self.previous_button.setText(str(update))
        self.lineEdit_number.setText(str(update))


    def xuly_xoa_gia_tri_am(self):
        self.list = [e for e in self.list if e >= 0]
        self.createRandom()


    def xuly_sort_asc(self):
        self.list.sort()
        self.createRandom()

    def xuly_sort_desc(self):
        self.list.sort(reverse=True)
        self.createRandom()

    def xuly_remove_all(self):
        self.clearLayout(self.verticalLayout)
        self.list = []
