import functools
from random import *

from PyQt6.QtWidgets import QPushButton

from Chuong2_cautrucdulieu.BT39.ui.MainWindow39 import Ui_MainWindow

class MainWindow39Ext(Ui_MainWindow):
    def __init__(self):
        self.list=[]
        self.previous_button=None
        self.select_index=-1

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_Create.clicked.connect(self.xuly_tao_ngaunhien)
        self.pushButton_delete.clicked.connect(self.xuly_xoa_button_dang_chon)


    def xuly_tao_ngaunhien(self):
        n=int(self.lineEdit_number)
        self.list=[random.randrange(-100, 101) for x in range(0, n)]
        self.createRandom()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.createRandom(item.layout())

    def createRandom(self):
        self.clearLayout(self.verticalLayout)
        for i in range(len(self.list)):
            x = self.list[i]
            print(x)
            title = f"{x}"
            btn = QPushButton(text=title)
            btn.setStyleSheet("background-color: rgb(237, 255, 127);")
            self.verticalLayout.addWidget(btn)
            btn.clicked.connect(functools.partial(self.doi_mau_nen,i))

    def doi_mau_nen(self,i):
        sender=self.MainWindow.sender()
        if self.previous_button !=None:#Tức là trước đó đã chọn
            self.previous_button.setStyleSheet("background-color: rgb(237, 255, 127);")
        sender.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.previous_button=sender
        #Hiển thị lại dữ liệu của button đang chọn lên linEdit
        self.lineEdit_number.setText(sender.text())
        self.select_index=i

    def xuly_xoa_button_dang_chon(self):
        if self.select_index==-1:
            return
        self.list.pop(self.select_index)
        self.select_index=-1
        self.previous_button=None
        self.lineEdit_number.setText("")
        self.createRandom()