import functools

from PyQt6.QtWidgets import QPushButton,QMainWindow

from Chuong2_cautrucdulieu.BT45.ui.MainWindow45 import Ui_MainWindow

from  search_title_window import  search_title_window

class MainWindow45Ext(Ui_MainWindow):
    def __init__(self):
        self.verticalLayoutBook = None
        self.books=[]
        self.previous_button = None
        self.select_index = -1
        self.SecondWindow = None

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
                    self.clearLayout(item.layout())

    #def createRandom(self, param):
      #  pass

    def setupSignalAndSlot(self):
        self.pushButton_Save.clicked.connect(self.xuly_luu_sach)
        self.pushButton_Remove.clicked.connect(self.xuly_xoa_book_dang_chon)
        self.pushButton_Search_title.clicked.connect(self.opensearch_title_window)
       # self.pushButton_Search_title.clicked.connect(self.xuly_searche_isbn)
        #self.pushButton_Filter_year.clicked.connect(self.xuly_loc_theo_year)
        #self.pushButton_Filter_publisher.clicked.connect(self.xuly_loc_theo_publisher)


    def xuly_luu_sach(self):
        for book in self.books:
            if book["isbn"] == self.lineEdit_ISBN.text():
                book["title"] = self.lineEdit_Title.text()
                book["author"] = self.lineEdit_Author.text()
                book["publisher"] = self.lineEdit_Publisher.text()
                book["year"] = self.lineEdit_Year.text()
                self.hien_thi_sach_len_giao_dien()
                return

        new_book = {"isbn": self.lineEdit_ISBN.text(),
                    "title": self.lineEdit_Title.text(),
                    "author": self.lineEdit_Author.text(),
                    "year": self.lineEdit_Year.text(),
                    "publisher": self.lineEdit_Publisher.text()}

        self.books.append(new_book)
        self.hien_thi_sach_len_giao_dien()


    def hien_thi_sach_len_giao_dien (self):
        #xóa toàn bộ sách trong layout đi để nạp lại
        self.clearLayout(self.verticalLayoutBook)
        for i in range(len(self.books)):
            book=self.books[i]
            book_button=QPushButton(text=book["title"])
            book_button.setStyleSheet("background-color: rgb(237, 255, 127);")
            book_button.clicked.connect(functools.partial(self.doi_mau_nen, i))
            book_button.clicked.connect(functools.partial(self.xem_chi_tiet,i))
            self.verticalLayoutBook.addWidget(book_button)


    def xem_chi_tiet (self, i):
        book=self.books[i]
        self.lineEdit_Title.setText(book["title"])
        self.lineEdit_Author.setText(book["author"])
        self.lineEdit_Publisher.setText(book["publisher"])
        self.lineEdit_ISBN.setText(book["isbn"])
        self.lineEdit_Year.setText(book["year"])


    def doi_mau_nen(self, i):
        sender = self.MainWindow.sender()
        if self.previous_button is not None:  # Reset previous button style
            self.previous_button.setStyleSheet("background-color: rgb(237, 255, 127);")
        sender.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.previous_button = sender
        self.lineEdit_ISBN.setText(sender.text())
        self.select_index = i

    def xuly_xoa_book_dang_chon(self):
        if self.select_index == -1:
            return
        self.books.pop(self.select_index)
        self.hien_thi_sach_len_giao_dien()
        self.lineEdit_ISBN.setText("")
        self.lineEdit_Title.setText("")
        self.lineEdit_Author.setText("")
        self.lineEdit_Publisher.setText("")
        self.lineEdit_Year.setText("")
        self.previous_button = None
        self.select_index = -1


    def open_search_title_window(self):
        self.search_window = search_title_window(self)
        self.search_window.setupUi(QMainWindow())
        self.search_window.MainWindow.show()
