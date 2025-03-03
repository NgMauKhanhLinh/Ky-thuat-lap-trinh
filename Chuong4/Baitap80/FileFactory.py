import traceback

from Chuong4_File.Baitap80.Product import Product


class FileFactory:
    @staticmethod
    def writeData(path, product):
        try:
            line = f"{product.productId};{product.productName};{product.unitPrice}\n"
            with open(path, 'a', encoding='utf-8') as file:
                file.write(line)
            return True
        except Exception as e:
            traceback.print_exc()
            return False

    @staticmethod
    def readData(path):
        products = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    data = line.strip().split(';')
                    if len(data) == 3:
                        product = Product(data[0], data[1], float(data[2]))
                        products.append(product)
            return products
        except Exception as e:
            traceback.print_exc()
            return []
