from PyQt6.QtWidgets import QApplication, QMainWindow

from LearnSignalsAndSlots import Ui_MainWindow

app=QApplication([])

qMainWindow=QMainWindow()

myWindow=Ui_MainWindow()

myWindow.setupUi(qMainWindow)

qMainWindow.show()

app.exec()