# Form implementation generated from reading ui file 'D:\pythonProject\KTLT_THAY_THANH\CHUONG5_GUI\ProductManagement\ui\ProductMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 596)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidgetCategory = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidgetCategory.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidgetCategory.setObjectName("listWidgetCategory")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetCategory.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetCategory.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.listWidgetCategory.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetCategory.addItem(item)
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setBackground(brush)
        self.listWidgetCategory.addItem(item)
        self.horizontalLayout.addWidget(self.listWidgetCategory)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidgetProduct = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidgetProduct.setMaximumSize(QtCore.QSize(16777215, 280))
        self.tableWidgetProduct.setObjectName("tableWidgetProduct")
        self.tableWidgetProduct.setColumnCount(5)
        self.tableWidgetProduct.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setItem(4, 4, item)
        self.verticalLayout_3.addWidget(self.tableWidgetProduct)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEditProductId = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditProductId.setGeometry(QtCore.QRect(100, 20, 271, 20))
        self.lineEditProductId.setObjectName("lineEditProductId")
        self.lineEditProductName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditProductName.setGeometry(QtCore.QRect(100, 50, 271, 20))
        self.lineEditProductName.setObjectName("lineEditProductName")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.label_3.setObjectName("label_3")
        self.lineEditPrice = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditPrice.setGeometry(QtCore.QRect(100, 80, 271, 20))
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.label_4.setObjectName("label_4")
        self.lineEditQuantity = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditQuantity.setGeometry(QtCore.QRect(100, 110, 271, 20))
        self.lineEditQuantity.setObjectName("lineEditQuantity")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 81, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditCateId = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditCateId.setGeometry(QtCore.QRect(100, 140, 271, 20))
        self.lineEditCateId.setObjectName("lineEditCateId")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.label_6.setObjectName("label_6")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSave.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonClear.setGeometry(QtCore.QRect(190, 170, 75, 23))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonRemove.setGeometry(QtCore.QRect(280, 170, 75, 23))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Product Management"))
        __sortingEnabled = self.listWidgetCategory.isSortingEnabled()
        self.listWidgetCategory.setSortingEnabled(False)
        item = self.listWidgetCategory.item(0)
        item.setText(_translate("MainWindow", "Cate 1"))
        item = self.listWidgetCategory.item(1)
        item.setText(_translate("MainWindow", "Cate 2"))
        item = self.listWidgetCategory.item(2)
        item.setText(_translate("MainWindow", "Cate 3"))
        item = self.listWidgetCategory.item(3)
        item.setText(_translate("MainWindow", "Cate 4"))
        item = self.listWidgetCategory.item(4)
        item.setText(_translate("MainWindow", "Cate 5"))
        self.listWidgetCategory.setSortingEnabled(__sortingEnabled)
        item = self.tableWidgetProduct.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetProduct.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetProduct.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidgetProduct.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidgetProduct.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidgetProduct.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Id"))
        item = self.tableWidgetProduct.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidgetProduct.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Unit Price"))
        item = self.tableWidgetProduct.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidgetProduct.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cate Id"))
        __sortingEnabled = self.tableWidgetProduct.isSortingEnabled()
        self.tableWidgetProduct.setSortingEnabled(False)
        item = self.tableWidgetProduct.item(0, 0)
        item.setText(_translate("MainWindow", "p1"))
        item = self.tableWidgetProduct.item(0, 1)
        item.setText(_translate("MainWindow", "Product 1"))
        item = self.tableWidgetProduct.item(0, 2)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidgetProduct.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetProduct.item(0, 4)
        item.setText(_translate("MainWindow", "c1"))
        item = self.tableWidgetProduct.item(1, 0)
        item.setText(_translate("MainWindow", "p2"))
        item = self.tableWidgetProduct.item(1, 1)
        item.setText(_translate("MainWindow", "Product 2"))
        item = self.tableWidgetProduct.item(1, 2)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidgetProduct.item(1, 3)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetProduct.item(1, 4)
        item.setText(_translate("MainWindow", "c2"))
        item = self.tableWidgetProduct.item(2, 0)
        item.setText(_translate("MainWindow", "p3"))
        item = self.tableWidgetProduct.item(2, 1)
        item.setText(_translate("MainWindow", "Product 3"))
        item = self.tableWidgetProduct.item(2, 2)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidgetProduct.item(2, 3)
        item.setText(_translate("MainWindow", "30"))
        item = self.tableWidgetProduct.item(2, 4)
        item.setText(_translate("MainWindow", "c3"))
        item = self.tableWidgetProduct.item(3, 0)
        item.setText(_translate("MainWindow", "p4"))
        item = self.tableWidgetProduct.item(3, 1)
        item.setText(_translate("MainWindow", "Product 4"))
        item = self.tableWidgetProduct.item(3, 2)
        item.setText(_translate("MainWindow", "50"))
        item = self.tableWidgetProduct.item(3, 3)
        item.setText(_translate("MainWindow", "37"))
        item = self.tableWidgetProduct.item(3, 4)
        item.setText(_translate("MainWindow", "c4"))
        item = self.tableWidgetProduct.item(4, 0)
        item.setText(_translate("MainWindow", "p5"))
        item = self.tableWidgetProduct.item(4, 1)
        item.setText(_translate("MainWindow", "Product 5"))
        item = self.tableWidgetProduct.item(4, 2)
        item.setText(_translate("MainWindow", "82"))
        item = self.tableWidgetProduct.item(4, 3)
        item.setText(_translate("MainWindow", "30"))
        item = self.tableWidgetProduct.item(4, 4)
        item.setText(_translate("MainWindow", "c5"))
        self.tableWidgetProduct.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Product Detail:"))
        self.label_2.setText(_translate("MainWindow", "Product Id:"))
        self.label_3.setText(_translate("MainWindow", "Product Name:"))
        self.label_4.setText(_translate("MainWindow", "Price:"))
        self.label_5.setText(_translate("MainWindow", "Quantity:"))
        self.label_6.setText(_translate("MainWindow", "Cate Id:"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
