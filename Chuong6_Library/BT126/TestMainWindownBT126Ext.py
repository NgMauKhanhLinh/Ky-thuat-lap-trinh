# from PyQt6.QtWidgets import QApplication, QMainWindow
#
# from MainWindownBT126Ext import MainWindownBT126Ext
#
# app=QApplication([])
# mainwindow=QMainWindow()
# myui=MainWindownBT126Ext()
# myui.setupUi(mainwindow)
# myui.showWindow()
# app.exec()


from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindownBT126Ext import MainWindownBT126Ext

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindownBT126Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
