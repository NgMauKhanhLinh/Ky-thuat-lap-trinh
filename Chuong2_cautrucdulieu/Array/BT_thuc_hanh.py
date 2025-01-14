import array as arr

arr_int=arr.array("i",[3,7,2,10,5])
print("Danh sách của ar_int:")
print ("Xuất từng phần tử theo index:")
for i in range (len(arr_int)):
    x=arr_int[i]
    print (x,end="")

print("\n Xuất giá trị có in theo cột:")
print("INDEX\t Value")
for i in range (len(arr_int)):
    x=arr_int[i]
    print(f"{i}\t\t{x}")
sum=0
for x in arr_int:
    sum+=x
print("Tổng mảng=" sum)
arr_int[3]=999
#arr_int.remove(10)
arr_int.pop(2)
for x in arr_int:
    print(x,end="")
#Sắp xếp mảng tăng dần
for i in range(len(arr_int)):
    for j in range(i+1,len(arr_int)):
        if arr_int[i]>arr_int[j]:
            temp=arr_int[i]
            arr_int[i]=arr_int[j]
            arr_int[j]=temp
print("\n Mảng sau khi sắp xếp:")
for x in arr_int:
    print(x,end="")