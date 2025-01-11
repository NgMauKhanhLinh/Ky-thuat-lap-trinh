from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong1_ham.Baitap.BT23.ui.MainWindow23Ext import MainWindow23Ext


app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindow23Ext()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()