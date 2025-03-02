import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from Chuong4.Baitap85.lib.DataConnector import DataConnector
from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Asset import Asset
from Chuong4.Baitap85.models.Employee import Employee
from Chuong4.Baitap85.ui.MainWindow85 import Ui_MainWindow


class MainWindow85Ext(Ui_MainWindow):
    def __init__(self):
        self.dc = DataConnector()
        self.assets = self.dc.get_all_asset()
        self.selected_asset = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.setupSignalandSlot()

        self.hienthi_sanpham_len_giaodien()

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

    def hienthi_sanpham_len_giaodien(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.assets)):
            sp = self.assets[i]
            btn = QPushButton(text=str(sp))
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet, sp))

    def xem_chi_tiet(self, sp):
        self.lineEditId.setText(sp.AssetId)
        self.lineEditName.setText(sp.AssetName)
        self.lineEditYear.setText(str(sp.Year))
        self.lineEditValue.setText(str(sp.Value))
        self.selected_asset = sp

    def setupSignalandSlot(self):
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.pushButtonSave.clicked.connect(self.xuly_luu)

    def xuly_xoa(self):
        msp = self.lineEditId.text()

        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xóa")
        dlg.setText(f"Muốn xóa [{msp}] hả?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.No:
            return  # ngừng hàm xóa, không làm gì cả

        if self.selected_asset != None:
            self.assets.remove(self.selected_asset)
            # cap nhat lai CSDL sau khi xoa
            # can luu lai co so du lieu
            jff = JsonFileFactory()
            filename = "../dataset/assets.Json"
            jff.write_data(self.assets, filename)

            self.hienthi_sanpham_len_giaodien()

    def xuly_luu(self):
        id = self.lineEditId.text()
        name = self.lineEditName.text()
        year = self.lineEditYear.text()
        value = self.lineEditValue.text()
        a = Asset(id, name, year, value)
        self.assets.append(a)
        jff = JsonFileFactory()
        filename = "../dataset/assets.Json"
        jff.write_data(self.assets, filename)
        self.hienthi_sanpham_len_giaodien()