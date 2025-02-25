import random

from CHUONG5_GUI.ProductManagement.lib.JsonFileFactory import JsonFileFactory
from CHUONG5_GUI.ProductManagement.model.Product import Product

products=[]

jff=JsonFileFactory()
filename="../Dataset/products.json"
products=jff.read_data(filename,Product)

print("List of Product after reading Json:")
for product in products:
    print(product)