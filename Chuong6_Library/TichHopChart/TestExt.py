from PyQt6.QtWidgets import QApplication, QMainWindow

from TichHopChart.MainWindowExt import MainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()