from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSubmit.clicked.connect(self.processSubmit)
    def show(self):
        self.MainWindow.show()
    def processSubmit(self):
        str=[]
        if self.chkMachineLearning.isChecked()==True:
            str.append(self.chkMachineLearning.text())
        if self.chkDeepLearning.isChecked()==True:
            str.append(self.chkDeepLearning.text())
        if self.chkSmartContract.isChecked()==True:
            str.append(self.chkSmartContract.text())
        separator=','
        infor="Full Name = "+self.lineEditFullName.text()+"\n"
        infor+="Email = "+self.lineEditEmail.text()+"\n"
        infor+="Selected courses:"+"\n"
        infor+=separator.join(str)
        self.msg=QMessageBox()
        self.msg.setWindowTitle("Selected Courses")
        self.msg.setText(infor)

        self.msg.show()