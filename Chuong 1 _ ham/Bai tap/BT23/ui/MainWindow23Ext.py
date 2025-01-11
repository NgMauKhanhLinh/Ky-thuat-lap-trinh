import traceback

from Chuong1_ham.Baitap.BT23.ui.MainWindow23 import Ui_MainWindow


class MainWindow23Ext(Ui_MainWindow):
    def __init__(self):
        self.so_khach_hang=0
        self.so_khach_hang_sv=0
        self.soluong_mua_khach_hang=0
        self.soluong_mua_khach_hang_sv=0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_BANMOI.clicked.connect(self.xuly_banmoi)
        self.pushButton_TINH.clicked.connect(self.xuly_tinhtien)
        self.pushButton_THONGKE.clicked.connect(self.xuly_thongke)
    def xuly_banmoi(self):
        try:
            self.lineEditTEN.setText("")
            self.lineEdit_SL.setText("")
            self.checkBox_SINHVIEN.setChecked(False)
            self.lineEdit_THANHTIEN.setText("")
            self.lineEditTEN.setFocus()
        except:
            traceback.print_exc()
    def xuly_tinhtien(self):
        name=self.lineEditTEN.text()
        quantity=int(self.lineEdit_SL.text())
        if self.checkBox_SINHVIEN.isChecked()==True:
            self.so_khach_hang_sv=self.so_khach_hang_sv+1
            self.soluong_mua_khach_hang_sv=self.soluong_mua_khach_hang_sv+quantity
            money=quantity*20000*0.95
            self.lineEdit_THANHTIEN.setText(f"{money}")
        else:
            self.so_khach_hang=self.so_khach_hang+1
            self.soluong_mua_khach_hang=self.soluong_mua_khach_hang+quantity
            money=quantity*20000
            self.lineEdit_THANHTIEN.setText(f"{money}")

    def xuly_thongke(self):
        total_money=self.so_khach_hang*self.soluong_mua_khach_hang*20000
        total_money_sv = self.so_khach_hang_sv * self.soluong_mua_khach_hang_sv*20000*0.95
        self.lineEdit_TONG_KH.setText(f"{self.so_khach_hang}")
        self.lineEdit_TONG_KHSV.setText(f"{self.so_khach_hang_sv}")
        self.lineEdit_DOANHTHU.setText(f"{total_money+total_money_sv}")


