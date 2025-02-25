from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem
from PyQt6.QtWidgets import QComboBox

from CHUONG5_GUI.ProductManagement.lib.DataConnector import DataConnector
from CHUONG5_GUI.ProductManagement.lib.JsonFileFactory import JsonFileFactory
from CHUONG5_GUI.ProductManagement.model.Product import Product
from CHUONG5_GUI.ProductManagement.test.TestProduct_WriteJson import prodid, product
from CHUONG5_GUI.ProductManagement.ui.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.categories=self.dc.get_all_categories()
        self.products=self.dc.get_all_products()
        self.selected_cate=None
        self.cboCategory = QComboBox(self)
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_categories_ui()
        self.show_products_ui()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def show_categories_ui(self):
        #remove existing data from QListWidget:(clear all previous data)
        self.listWidgetCategory.clear()
        #add cate item into QListWidget by for:
        for cate in self.categories:
            cate_item=QListWidgetItem(str(cate))
            self.listWidgetCategory.addItem(cate_item)

    def show_products_ui(self):
        #remove existing data from QTable Widget
        self.tableWidgetProduct.setRowCount(0)
        #add product item into QTableWidget:
        for product in self.products:
            #return number of row (meaning: last row)
            row=self.tableWidgetProduct.rowCount()
            #insert a new row:
            self.tableWidgetProduct.insertRow(row)
            #create 5 columns:
            col_prodid=QTableWidgetItem(product.prodid)
            col_prodname=QTableWidgetItem(product.prodname)
            col_price=QTableWidgetItem(str(product.price))
            col_quantity=QTableWidgetItem(str(product.quantity))
            col_cateid=QTableWidgetItem(str(product.cateid))
            #set cell for row:
            self.tableWidgetProduct.setItem(row,0,col_prodid)
            self.tableWidgetProduct.setItem(row,1,col_prodname)
            self.tableWidgetProduct.setItem(row,2,col_price)
            self.tableWidgetProduct.setItem(row,3,col_quantity)
            self.tableWidgetProduct.setItem(row,4,col_cateid)

            if product.price>=800 and product.price<=1000:
                col_prodid.setBackground(Qt.GlobalColor.red)
                col_prodname.setBackground(Qt.GlobalColor.red)
                col_price.setBackground(Qt.GlobalColor.red)
                col_quantity.setBackground(Qt.GlobalColor.red)
                col_cateid.setBackground(Qt.GlobalColor.red)

    def setupSignalAndSlot(self):
        self.listWidgetCategory.itemSelectionChanged.connect(self.process_filter_products)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.process_show_product_detail)
        self.pushButtonClear.clicked.connect(self.clear_detail_data)
        self.pushButtonSave.clicked.connect(self.save_product_infor)
        self.pushButtonRemove.clicked.connect(self.remove_product)
        self.cboCategory.activated.connect(self.processSelectedComboBox)
    def process_filter_products(self):
        #get current select index
        row=self.listWidgetCategory.currentRow()
        if row<0: #not found selected index
            return
        self.selected_cate=self.categories[row]
        #filter products by cate id
        self.products=self.dc.get_product_by_category(self.selected_cate.cateid)
        #re-display product into QTableWidget
        self.show_products_ui()

    def process_show_product_detail(self):
        index = self.tableWidgetProduct.currentRow()
        if index < 0:
            return
        product = self.products[index]
        self.lineEditProductId.setText(product.prodid)
        self.lineEditProductName.setText(product.prodname)
        self.lineEditPrice.setText(str(product.price))
        self.lineEditQuantity.setText(str(product.quantity))
        self.lineEditCateId.setText(str(product.cateid))

    def clear_detail_data(self):
        self.lineEditProductId.clear()
        self.lineEditProductName.clear()
        self.lineEditPrice.clear()
        self.lineEditQuantity.clear()
        self.lineEditCateId.clear()
        self.lineEditProductId.setFocus()

    def save_product_infor(self):
        # Step 1: get user input information:
        prodid = self.lineEditProductId.text()
        prodname = self.lineEditProductName.text()
        price = float(self.lineEditPrice.text())
        quantity = int(self.lineEditQuantity.text())
        cateid = self.lineEditCateId.text()
        # Step 2: create Object Model
        self.products = self.dc.get_all_products()
        p = Product(prodid, prodname, price, quantity, cateid)
        index = self.dc.check_existing_product(self.products, product.prodid)
        if index == -1:  # not found-->insert new
            self.products.append(p)
        else:  # found -> update
            self.products[index] = p
        # Step 3: Save all object into Hard disk:
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        jff.write_data(self.products, filename)
        # Step 4: Re-display data into GUI:
        if self.selected_cate != None:
            self.products = self.dc.get_product_by_category(self.selected_cate.cateid)
        else:
            self.products = self.dc.get_product_by_category(product.cateid)
        self.show_products_ui()

    def remove_product(self):
        # Step 1: Find the product that we want to remove it
        prodid = self.lineEditProductId.text()
        self.products = self.dc.get_all_products()
        index = self.dc.check_existing_product(self.products, prodid)
        if index == -1:  # not found->then end the algorithm
            return
        # Step 2: Remove product by index
        self.products.pop(index)
        # Step 3: Save all data into Hard Disk:
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        jff.write_data(self.products, filename)
        # Step 4: Re-display data into GUI:
        if self.selected_cate != None:
            self.products = self.dc.get_product_by_category(self.selected_cate.cateid)
        else:
            self.products = self.dc.get_all_products()
        self.show_products_ui()
        self.clear_detail_data()

    self.cboCategory.addItem('Laptop')
    self.cboCategory.addItem('Phone & Tablet')
    self.cboCategory.addItem('Smart Watch')
    self.cboCategory.insertItem(1, "Head Phone")