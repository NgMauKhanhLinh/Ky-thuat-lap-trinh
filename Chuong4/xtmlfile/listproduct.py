from xml.dom.minidom import parse

from Chuong4.xtmlfile.Product import Product


class ListProduct:
    def __init__(self):
        self.products=[]
    def print_all_products(self):
        for p in self.products:
            print(p)
    def import_data_from_xml(self,filename):
        DOMTree = parse(filename)
        elements = DOMTree.documentElement

        products = elements.getElementsByTagName("product")
        for p in products:
            pro_id = (p.getElementsByTagName("id")[0]).childNodes[0].data
            pro_name = (p.getElementsByTagName("name")[0]).childNodes[0].data
            pro_price = (p.getElementsByTagName("price")[0]).childNodes[0].data
            print(pro_id + " -> " + pro_name + " -> " + pro_price)
            self.products.append(Product(pro_id,pro_name,pro_price))