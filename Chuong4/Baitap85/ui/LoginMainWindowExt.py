from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Chuong4.Baitap85.lib.DataConnector import DataConnector
from Chuong4.Baitap85.ui.LoginMainWindow import Ui_MainWindow
from Chuong4.Baitap85.ui.MainWindow85Ext import MainWindow85Ext


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_login.clicked.connect(self.process_login)
    def process_login(self):
        dc=DataConnector()
        uid = self.lineEdit_username.text()
        pwd = self.lineEdit_password.text()
        emp = dc.login(uid, pwd)
        if emp != None:
            self.MainWindow.close()#close login window
            mainwindow = QMainWindow()
            self.myui = MainWindow85Ext()
            self.myui.setupUi(mainwindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()