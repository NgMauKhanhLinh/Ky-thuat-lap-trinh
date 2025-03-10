
import numpy as np

#khởi tạo
#vd1
arr=np.array([[1,3,5],[2,4,6]])
print(arr)
print(arr.shape) #kích thước mảng


#vd2
arr=np.array([[[1,3,5],[2,4,6]],[[10, 11, 12], [15, 20, 25]]])
print(arr)
print(arr.shape)

#vd3
arr= np.zeros([2,4,6], dtype=int)
print(arr)

#vd4
arr= np.zeros([2,4], dtype=int)
print(arr)



#Truy xuất
#vd1
arr = np. array([[[1,3,5],[2,4,6]],[[10, 11, 12], [15, 20, 25]]])
print (arr)
print(arr[0])
print(arr[1][0][2])
print(arr[1][1][1])


#vd2
arr = np. array([[[1,3,5],[2,4,6]],[[10, 11, 12], [15, 20, 25]]])
print (arr)
print(np.max(arr))
print(np.mean(arr[1]))
print(arr[np.where(arr>8)])



#cập nhật giá trị
#vd1
arr = np. array([[[1,3,5],[2,4,6]],[[10, 11, 12], [15, 20, 25]]])
print (arr)
print(arr[1][0])


#sắp xếp
arr = np. array([[[1,3,5],[2,4,6]],[[10, 11, 12], [15, 20, 25]]])
print(np.sort(arr))


#tính toán số học
#vd1
arr1 = np. array([[1,3,5],[2,4,6]])
arr2= np. array([1,3,5])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)


#chuyển đổi dòng <-> cột
#vd1
arr1 = np.array(range(12))
print(arr1)

#vd2
arr_reshape = arr1.reshape (3,5)
print(arr_reshape)

#vd3
arr2 = arr_reshape.reshape(2, -2)
print(arr2)

#vd4
arr3 = arr_reshape.flatten()
print(arr3)




