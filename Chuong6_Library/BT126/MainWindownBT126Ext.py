import pandas as pd
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from LearnPandas.BT126.MainBT126 import Ui_MainWindow

class MainWindownBT126Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.df = pd.read_csv("Data/TCB_2018_2020.csv")  # Đọc dữ liệu

        self.setupSignalsAndSlot()
        self.hien_thi_du_lieu_goc(self.df)  # Hiển thị dữ liệu ngay khi mở chương trình

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalsAndSlot(self):
        self.pushButtonLocClose.clicked.connect(self.loc_du_lieu)
        self.pushButtonNgay.clicked.connect(self.loc_theo_ngay)
        self.pushButtonLocDateHighLow.clicked.connect(self.loc_theo_low_range)

    def hien_thi_du_lieu_goc(self, data):
        """Hiển thị dữ liệu gốc lên QTableWidget khi mở chương trình"""
        self.tableWidgetResult.setRowCount(len(data))
        self.tableWidgetResult.setColumnCount(len(data.columns))
        self.tableWidgetResult.setHorizontalHeaderLabels(data.columns)

        for i, row in data.iterrows():
            for j, value in enumerate(row):
                self.tableWidgetResult.setItem(i, j, QTableWidgetItem(str(value)))

    def loc_du_lieu(self):
        """Lọc dữ liệu theo Close < x và Close > y"""
        try:
            input_text = self.lineEditInput.text().strip()
            if not input_text or "," not in input_text:
                QMessageBox.warning(self.MainWindow, "Lỗi",
                                    "Vui lòng nhập hai số hợp lệ, cách nhau bởi dấu phẩy (x, y).")
                return

            try:
                x, y = map(float, input_text.split(","))
            except ValueError:
                QMessageBox.warning(self.MainWindow, "Lỗi",
                                    "Dữ liệu không hợp lệ. Vui lòng nhập hai số hợp lệ cách nhau bởi dấu phẩy.")
                return

            # Loại bỏ các giá trị NaN trong cột "Close"
            self.df["Close"] = pd.to_numeric(self.df["Close"], errors="coerce")
            self.df = self.df.dropna(subset=["Close"])

            # Lọc dữ liệu với điều kiện Close < x và Close > y
            filtered_df = self.df[(self.df["Close"] < x) & (self.df["Close"] > y)]

            if filtered_df.empty:
                QMessageBox.information(self.MainWindow, "Thông báo", "Không có dữ liệu thỏa mãn điều kiện lọc.")
                return

            self.hien_thi_du_lieu(filtered_df)

            # Hiển thị thông báo lọc thành công
            QMessageBox.information(self.MainWindow, "Thành công", "Lọc dữ liệu thành công!")

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi không xác định", str(e))

    def loc_theo_ngay(self):
        """Lọc dữ liệu theo danh sách ngày nhập vào (DD-MM-YYYY), cách nhau bằng dấu phẩy"""
        try:
            input_text = self.lineEditInput.text().strip()
            if not input_text:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập ít nhất một ngày (DD-MM-YYYY).")
                return

            date_list = [date.strip() for date in input_text.split(",")]

            # Kiểm tra định dạng nhập vào
            formatted_dates = []
            for date in date_list:
                try:
                    formatted_dates.append(pd.to_datetime(date, format="%d-%m-%Y").strftime("%Y-%m-%d"))
                except ValueError:
                    QMessageBox.warning(self.MainWindow, "Lỗi",
                                        f"Định dạng ngày không hợp lệ: {date}. Vui lòng nhập theo định dạng DD-MM-YYYY.")
                    return

            filtered_df = self.df[self.df["Date"].isin(formatted_dates)]

            if filtered_df.empty:
                QMessageBox.information(self.MainWindow, "Thông báo", "Không có dữ liệu cho các ngày đã nhập.")
            else:
                self.hien_thi_du_lieu(filtered_df)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi không xác định", str(e))

    def hien_thi_du_lieu(self, data):
        """Hiển thị dữ liệu lọc lên QTableWidget"""
        self.tableWidgetResult.setRowCount(len(data))
        self.tableWidgetResult.setColumnCount(len(data.columns))
        self.tableWidgetResult.setHorizontalHeaderLabels(data.columns)

        for i, row in data.iterrows():
            for j, value in enumerate(row):
                self.tableWidgetResult.setItem(i, j, QTableWidgetItem(str(value)))

    def loc_theo_low_range(self):
        """Lọc dữ liệu lấy Date, High, Low với giá trị Low từ x đến y"""
        try:
            input_text = self.lineEditInput.text().strip()
            if not input_text or "," not in input_text:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập hai số, cách nhau bởi dấu phẩy (x, y).")
                return

            try:
                x, y = map(float, input_text.split(","))
            except ValueError:
                QMessageBox.warning(self.MainWindow, "Lỗi",
                                    "Dữ liệu không hợp lệ. Vui lòng nhập hai số hợp lệ cách nhau bởi dấu phẩy.")
                return

            # Lọc dữ liệu chỉ lấy các cột cần thiết và khoảng Low từ x đến y
            filtered_df = self.df[["Date", "High", "Low"]]
            filtered_df = filtered_df[(filtered_df["Low"] >= x) & (filtered_df["Low"] <= y)]

            if filtered_df.empty:
                QMessageBox.information(self.MainWindow, "Thông báo", "Không có dữ liệu thỏa mãn điều kiện lọc.")
                return

            self.hien_thi_du_lieu(filtered_df)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi không xác định", str(e))

