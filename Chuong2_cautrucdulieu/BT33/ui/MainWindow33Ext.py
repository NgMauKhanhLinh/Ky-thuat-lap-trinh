from random import randint

from PyQt6.QtWidgets import QMessageBox

from PyQt6.QtWidgets import QDialog

from Chuong2_cautrucdulieu.BT33.ui.MainWindow33 import Ui_MainWindow


class MainWindow33Ext(Ui_MainWindow):
    def __init__(self):
        self.array_int=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()


    def setupSignalAndSlot(self):
        self.pushButton_thoat.clicked.connect(self.xuly_thoat)
        self.pushButton_xuatmangngaunhien.clicked.connect(self.xuly_xuatmang_ngaunhien)
        self.pushButton_tongmang.clicked.connect(self.xuly_tinhtongmang)

    def xuly_thoat(self):
        dlg = QDialog()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass

    def xuly_xuatmang_ngaunhien(self):
        x = [randint(-100,100) for p in range(0,10)]
        self.array_int= array('i',x)
        s=""
        for i in self.array_int:
            s+=str(item)+" "
        self.lineEdit_manggoc.setText(s)

    def xuly_tinhtongmang(self):
        sum=0
        for x in self.array_int:
            sum=+x
            self.lineEdit_ketqua.setText(f"Tổng mảng= {sum}")
