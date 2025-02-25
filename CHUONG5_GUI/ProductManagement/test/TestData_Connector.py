from CHUONG5_GUI.ProductManagement.lib.DataConnector import DataConnector

dc=DataConnector()
categories=dc.get_all_categories()
print("List of Categories in database:")
for cate in categories:
    print(cate)
products=dc.get_all_products()
print("List of Products in database:")
for product in products:
    print(product)

c10="c10"
products_c10=dc.get_product_by_category(c10)
print("*"*20)
print("List of Products by Category =c10:")
for product in products_c10:
    print(product)
print("=>",len(products_c10))