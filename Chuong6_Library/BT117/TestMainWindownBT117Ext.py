from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindownBT117Ext import MainWindownBT117Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindownBT117Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()