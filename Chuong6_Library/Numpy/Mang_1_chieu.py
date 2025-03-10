import numpy as np

#Hàm np.array()
arr1 = np.array([6, 6.5, 4, 5.5, 7, 8.5])
print(arr1)
print(type(arr1))
print(arr1.dtype)



#Hàm np.asarray()
list_sample = [5, 7, 6.5, 8, 9.5]
tuple_sample = (6, 4, 5.5, 8.5)
arr2 = np.asarray(list_sample)
arr3 = np.asarray(tuple_sample)
print(arr2)
print(arr3)


# hàm np.zeros(), np.ones()
arr_zeros = np.zeros(4)
arr_ones = np.ones(3, dtype=int)
print(arr_zeros)
print(arr_ones)



#hàm np.arange (start, stop, step, dtype)
arr1 = np.arange(2,10,1.5)
arr2 = np.arange(6)
print(arr1)
print(arr2)


#hàm np.linspace(start, stop, num, endpoint, dtype)
arr = np.linspace(5, 15, 6)
print(arr)


#hàm np.random.rand() / randn()/ randint()
arr1 = np.arange(3)
arr2 = np.arange(7)
arr3 = np.arange(12, 42, 6)
print(arr1)
print(arr2)
print(arr3)

#hàm np.random.uniform (low, high, size)
ar1= np.random.uniform(0.5, 5.1, 50)
print(ar1)

#hàm np.random.normal (loc, scale, size)
ar2 = np.random.normal(5.2, 1.1, 1000)
print(ar2)


#truy xuất ví dụ
arr= np.random.randint (12,88, 9)
print(arr)
print(arr[1])
print(arr[-2])
print(arr[[1, 3, 4]])
print(arr[2:5])
print(arr[arr<40])


#truy xuất giá trị thống kê cơ bản
arr = np.random.randint(6, 40, 5)
print(arr)
print(np.min(arr))
print(np.argmin(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))


#Thêm phần tử
arr = np.array([5, 3, 16, 8, 10, 6, 12, 9])
print(arr)
arr = np.append(arr, [6, 3])
print(arr)
arr = np.insert(arr, 2, [6, 1])
print(arr)


#xóa phần tử
arr = np.array([5, 3, 16, 8, 10, 6, 12, 9])
arr = np.delete(arr, [2, 4])
print(arr)


#sắp xếp
arr = np.array([5, 3, 16, 8, 10, 6, 12, 9])
print(np.sort(arr))
print(np.sort(arr)[::-1])


#tính toán số học
arr1 = np.array([1, 3, 6])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)


