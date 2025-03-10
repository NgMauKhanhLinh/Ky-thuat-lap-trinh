import numpy as np

arr = np.random.randint(-100, 501,10)
print(arr)                  #xuất toàn bộ
print(arr[2:6])             #xuất từ 2 đến 5
print(arr[arr<0])           #xuất số âm cách 1
indices=np.where(arr<0)
print (arr[indices]) #xuất số âm cách 2


print(np.extract(arr<0,arr)) #xuất số âm cách 3

#câu 4
x=int(input())
y=int(input())

print(arr[arr>=x and arr<=y])