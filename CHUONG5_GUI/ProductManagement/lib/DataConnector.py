from CHUONG5_GUI.ProductManagement.lib.JsonFileFactory import JsonFileFactory
from CHUONG5_GUI.ProductManagement.model.Category import Category


class DataConnector:
    def get_all_categories(self):
        categories = []  # tao list
        jff = JsonFileFactory()
        filename = "../Dataset/categories.json"
        categories = jff.read_data(filename, Category)
        return categories
    def get_all_products(self):
        products = []
        jff = JsonFileFactory()
        filename = "../Dataset/products.json"
        from CHUONG5_GUI.ProductManagement.model.Product import Product
        products = jff.read_data(filename, Product)
        return products
    def get_product_by_category(self, cateid):
        products=self.get_all_products()
        result=[]
        for product in products:
            if product.cateid == cateid:
                result.append(product)
        return result

    def check_existing_product(self,products,prodid):
        for i in range(len(products)):
            product=products[i]
            if product.prodid==prodid:
                return i
        return -1
