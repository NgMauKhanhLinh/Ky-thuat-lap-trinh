import sys
import pandas as pd
from PyQt6.QtWidgets import QMessageBox, QApplication
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt import MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from MainWindown import Ui_MainWindow

class MainWindowExt (Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupPlot()
        self.pushButtonBarChart.clicked.connect(self.showBarChart)
        self.pushButtonLine.clicked.connect(self.showLinePlotChart)
        self.pushButtonPie.clicked.connect(self.showPieChart)
        self.pushButtonExit.clicked.connect(self.processExit)

    def showWindow(self):
        self.MainWindow.show()

    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

        # adding tool bar to the layout
        self.verticalLayoutPlot.addWidget(self.toolbar)
        # adding canvas to the layout
        self.verticalLayoutPlot.addWidget(self.canvas)

    def showBarChart(self):
        df = pd.read_csv('./Data/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style="plain")
        ax.grid()
        ax.bar(df["Year"], df["VNM"])
        ax.set_title("Bar chart title")
        # ax.set_xlabel(columnX)
        # ax.set_ylabel(columnY)
        self.canvas.draw()

    def showLinePlotChart(self):
        df = pd.read_csv('./Data/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style="plain")
        ax.grid()
        sns.lineplot(data=df, x="Year", y="VNM", marker='o', color='orange')
        ax.set_xlabel("Year")
        ax.set_ylabel("VNM")
        ax.set_title("SNS Line Plot Title")
        ax.legend(loc='lower right')
        self.canvas.draw()

    def showPieChart(self):
        df = pd.read_csv('./Data/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.pie(df["Year"], labels=df["VNM"], autopct='%1.2f%%')
        ax.legend(df["Year"], loc='lower right')
        ax.set_title("Pie Chart Title")
        self.canvas.draw()

    def processExit(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Chắc chắn muốn thoát phần mềm không?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()