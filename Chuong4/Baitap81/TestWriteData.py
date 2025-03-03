from FileFactory import FileFactory
from Product import Product

print("Nhập danh sách sản phẩm:")
while True:
    productId = input("Nhập mã sản phẩm: ")
    productName = input("Nhập tên sản phẩm: ")
    unitPrice = float(input("Nhập đơn giá: "))

    product = Product(productId, productName, unitPrice)
    FileFactory.writeData("database.txt", product)

    ans = input("Tiếp tục nhập? (Y/N): ").strip().lower()
    if ans != 'y':
        break
