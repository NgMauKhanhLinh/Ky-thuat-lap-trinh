import functools

from PyQt6.QtWidgets import QPushButton

from Chuong2_cautrucdulieu.BT45.ui.MainWindow45 import Ui_MainWindow


class MainWindow45Ext(Ui_MainWindow):
    def __init__(self):
        self.verticalLayoutBook = None
        self.books=[]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.createRandom(item.layout())

    def createRandom(self, param):
        pass

    def setupSignalAndSlot(self):
        self.pushButton_Save.clicked.connect(self.xuly_luu_sach)

    def xuly_luu_sach(self):
        book={"isbn":self.lineEdit_ISBN.text(),
               "title":self.lineEdit_Title.text(),
               "author":self.lineEdit_Author.text(),
               "publisher":self.lineEdit_Publisher.text()}
        self.books.append(book)
        self.hien_thi_sach_len_giao_dien()

    def hien_thi_sach_len_giao_dien(self):
        #xóa toàn bộ sách trong layout đi để nạp lại
        self.clearLayout(self.verticalLayoutBook)
        for i in range(len(self.books)):
            book=self.books[i]
            book_button=QPushButton(text=book["title"])
            self.verticalLayoutBook.addWidget(book_button)
            book_button.clicked.connect(functools.partial(self.xem_chi_tiet,i))

    def xem_chi_tiet(self, i):
        book=self.books[i]
        self.lineEdit_Title.setText(book["title"])
        self.lineEdit_Author.setText(book["author"])
        self.lineEdit_Publisher.setText(book["publisher"])
        self.lineEdit_ISBN.setText(book["isbn"])
        self.lineEdit_Year.setText(book["year"])