from lib2to3.btm_utils import reduce_tree


class Product:
    def __init__(self,id=None,name=None,prcie=None):
        self.id=id
        self.name=name
        self.price=prcie
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.price}"
