from PyQt6.QtWidgets import QMessageBox

from LearnQMainWindow import Ui_MainWindow

class MyQMainWindowExt(Ui_MainWindow):
    #override setupUi
    #just define attribute MainWindow for reuse in later
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    #define methods for assigning Signals and Slots
    def processSignalAndSlot(self):
        self.pushButtonThoat.clicked.connect(self.processExit)
    #define slot exit window
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit Confirmation")
        dlg.setText("Are you sure you want to Exit?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        # check the user confirmation
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass#do nothing