from xml.dom.minidom import parse

DOMTree = parse("product.xml")
elements = DOMTree.documentElement

products = elements.getElementsByTagName("product")
for p in products:
    pro_id = (p.getElementsByTagName("id")[0]).childNodes[0].data
    pro_name = (p.getElementsByTagName("name")[0]).childNodes[0].data
    pro_price = (p.getElementsByTagName("price")[0]).childNodes[0].data
    print(pro_id + " -> " + pro_name + " -> " + pro_price)

