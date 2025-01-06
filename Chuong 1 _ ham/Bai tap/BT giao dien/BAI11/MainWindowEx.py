from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        #change text
        self.changeTextpushButton.clicked.connect(self.processChangeText)
        #change font
        self.fontSizepushButton.clicked.connect(self.processChangeFontSize)
        #set align text
        self.alignLeftpushButton.clicked.connect(self.processAlignLeft)
        self.alignCenterpushButton.clicked.connect(self.processAlignCenter)
        self.alignRightpushButton.clicked.connect(self.processAlignRight)
        #change image with PNG format
        self.ShowPNGpushButton.clicked.connect(self.processChangePNG)
        #change image with gif format
        self.showGIFpushButton.clicked.connect(self.processChangeGIF)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.Titlelabel.setText("https://tranduythanh.com")
    def processChangeFontSize(self):
        #get font object
        font=self.Titlelabel.font()
        #change font size
        font.setPointSize(20)
        #set italic
        font.setItalic(True)
        #set bold
        font.setBold(True)
        #set font name
        font.setFamily("cambria")
        #re-assign font
        self.Titlelabel.setFont(font)
    def processAlignLeft(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangePNG(self):
        #create QPixmap instance
        pixmap=QPixmap("images/s303.PNG")
        #set pixmap for label
        self.imageLabel.setPixmap(pixmap)
    def processChangeGIF(self):
        #create QMovie instance
        movie=QMovie("images/cf6be01ff89bb72be179a537104984a5.gif")
        #set movie object for label
        self.imageLabel.setMovie(movie)
        #call start method
        movie.start()