from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong2_cautrucdulieu.BT33.ui.MainWindow33Ext import MainWindow33Ext

app=QApplication([])
MainWindow=QMainWindow()
myui=MainWindow33Ext()
myui.setupUi(MainWindow)
myui.showWindow()
app.exec()
