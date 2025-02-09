from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong1_ham.Baitap.MainWindow_BT21Ext import MainWindow_BT21Ext

app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindow_BT21Ext()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()