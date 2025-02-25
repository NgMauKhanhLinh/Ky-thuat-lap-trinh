from fileinput import filename

from CHUONG5_GUI.ProductManagement.lib.JsonFileFactory import JsonFileFactory
from CHUONG5_GUI.ProductManagement.model.Category import Category

categories=[]#tao list

jff=JsonFileFactory()
filename="../Dataset/categories.json"
categories=jff.read_data(filename,Category)
print("List of categories after reading Json:")
for cate in categories:
    print(cate)



