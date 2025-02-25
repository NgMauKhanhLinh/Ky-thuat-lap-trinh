from fileinput import filename

from CHUONG5_GUI.ProductManagement.lib.JsonFileFactory import JsonFileFactory
from CHUONG5_GUI.ProductManagement.model.Category import Category

categories=[]#tao list
for i in range(1,21):
    cate=Category(f"c{i}",f"Cate {i}")
    categories.append(cate)
print("List of Categories:")
for cate in categories:
    print(cate)
jff=JsonFileFactory()
filename="../Dataset/categories.json"
jff.write_data(categories,filename)


