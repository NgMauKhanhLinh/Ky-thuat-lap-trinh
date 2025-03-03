class Product:
    def __init__(self,productId,productName,unitPrice):
        self.productId=productId
        self.productName=productName
        self.unitPrice=unitPrice
    def __str__(self):
        return f"{self.productId}\t{self.productName}\t{self.unitPrice}"