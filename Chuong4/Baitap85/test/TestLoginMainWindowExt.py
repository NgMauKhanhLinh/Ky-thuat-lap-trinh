from PyQt6.QtWidgets import QMainWindow, QApplication

from Chuong4.Baitap85.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()