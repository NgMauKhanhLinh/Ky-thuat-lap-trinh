import random

from CHUONG5_GUI.ProductManagement.lib.JsonFileFactory import JsonFileFactory
from CHUONG5_GUI.ProductManagement.model.Product import Product

products=[]
for i in range(1,1001):
    prodid=f"P{i}"
    prodname=f"Product {i}"
    price=random.randrange(10,1000)
    quantity=random.randrange(1,10)
    cateid=f"c{random.randrange(1,21)}"
    p=Product(prodid,prodname,price,quantity,cateid)
    products.append(p)
print("List of Products:")
for product in products:
    print(product)
jff=JsonFileFactory()
filename="../Dataset/products.json"
jff.write_data(products,filename)