from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong2_cautrucdulieu.BT39.ui.MainWindow39Ext import MainWindow39Ext

app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindow39Ext()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()