import numpy as np

from BT117 import Ui_MainWindow


class MainWindownBT117Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalsAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.do_task)

    def do_task(self):
        s= self.lineEditInputData.text
        arr = s.split(',')
        print("Arr before casting Interger:")
        print(arr)
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        print("Arr after casting Interger:")
        print(arr)
        result=""
        result+="min"       +str(np.min(arr))   +"\n"
        result += "argmin" +str(np.argmin(arr)) +"\n"
        result += "max"     +str(np.max(arr))   +"\n"
        result += "argmax" +str(np.argmax(arr)) +"\n"
        result += "mean"    +str(np.mean(arr))  +"\n"
        result += "median" +str(np.median(arr)) +"\n"
        result += "std"     +str(np.std(arr))   +"\n"
        self.labelResults.setText(result)