class Product:
    def __init__(self, prodid,prodname, price, quantity, cateid):
        self.prodid = prodid
        self.prodname = prodname
        self.price = price
        self.quantity = quantity
        self.cateid = cateid
    def __str__(self):
        return f'{self.prodid}\t{self.prodname}\t{self.price}\t{self.quantity}\t{self.cateid}'
    