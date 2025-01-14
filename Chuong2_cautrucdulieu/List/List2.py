list1=[1,2,3]
list2=[4,5,6]

print("list1[1]=",list1[1])
#lệnh dưới dây gây ra 2 tình huống
#Alias
list1=list2
list2[1]=113
print("list1[1]=",list1[1])