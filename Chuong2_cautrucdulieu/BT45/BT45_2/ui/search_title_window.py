from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout


class search_title_window(object):
    def __init__(self, parent):
        self.parent = parent

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setWindowTitle("Nguyen Mau Khanh Linh - search_title_window")
        self.MainWindow.resize(381, 110)


        self.label = QLabel("Search Title:", parent=MainWindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))

        self.lineEdit_Title = QLineEdit(parent=MainWindow)
        self.lineEdit_Title.setGeometry(QtCore.QRect(20, 40, 351, 22))

        self.pushButton_Search = QPushButton("Search", parent=MainWindow)
        self.pushButton_Search.setGeometry(QtCore.QRect(40, 70, 93, 28))

        self.pushButtonClose = QPushButton("Close", parent=MainWindow)
        self.pushButtonClose.setGeometry(QtCore.QRect(250, 70, 93, 28))


        self.pushButton_Search.clicked.connect(self.xuly_search_title)
        self.pushButtonClose.clicked.connect(self.processClose)

    def xuly_search_title(self):
        title_to_search = self.lineEdit_Title.text()
        filtered_books = [book for book in self.parent.books if title_to_search.lower() in book["title"].lower()]


        self.parent.hien_thi_sach_len_giao_dien(filtered_books)

    def processClose(self):
        self.MainWindow.close()
        self.parent.secondWindow = None
