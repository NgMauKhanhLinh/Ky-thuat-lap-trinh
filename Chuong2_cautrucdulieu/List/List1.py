list1=["Obama","Kim Jong Un", "Putin"]
print("Duyệt danh sách theo đối tượng:")
for item in list1:
    print(item)
print("Duyệt danh sách theo chi mục:")
for i in range(len(list1)):
    item=list1[i]
    print(f"{i}=>{item}")

list2=[[1,2,3],
       [4,5,6],
       [7,8,9]]
print("Toàn bộ list2:")
print(list2)
print("Xuất ma trận theo mỗi dòng là 1 mảng:")
for row in list2:
    print(row)
print("Xuất ma trận theo mỗi ô của dòng:" )
for row in list2:
    for row in range(len(list2)):
        print(row[i],end=' ')
    print()
