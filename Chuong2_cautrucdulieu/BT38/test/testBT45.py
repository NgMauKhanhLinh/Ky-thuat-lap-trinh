from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong2_cautrucdulieu.BT45.ui.MainWindow45Ext import MainWindow45Ext

app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindow45Ext()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()