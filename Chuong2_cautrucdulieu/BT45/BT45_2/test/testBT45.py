from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong2_cautrucdulieu.BT45.ui.MainWindow45Ext import MainWindow45Ext
import sys
sys.path.append('D:\pythonProject\KTLT_THAY_THANH\Chuong2_cautrucdulieu\BT45')

app=QApplication([])
mainWindow=QMainWindow()
myui=MainWindow45Ext()
myui.setupUi(mainWindow)
myui.showWindow()
app.exec()