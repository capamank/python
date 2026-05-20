#operation on numpy array

import numpy as np
#reshaping array
arr=np.array([[1,2,3],[4,5,6]])
reshaped=arr.reshape(3,2)
print(reshaped,reshaped.shape)

#indexing on array

#1d array
arr=np.array([1,2,3,4,5])
print(arr[3])

#2d array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1[0][2])

#fancy indexing
idx=[1,2,3]
print(arr[idx])

#boolean indexing
print(arr[arr<2])
print(arr[arr%2==0])
print(arr[arr%2!=0])

# Slicing 1D array  
arr = np.array([1, 2, 3, 4, 5, 6, 7])  
print(arr[2:6])  # [3, 4, 5, 6]  
print(arr[:6])  # [1, 2, 3, 4, 5, 6]  
print(arr[3:])  # [4, 5, 6, 7]  
print(arr[::2])  # [1, 3, 5, 7] 

# Sliced List is a COPY  
py_list = [1, 2, 3, 4, 5]  
copy_list = py_list[1:4] # [2, 3, 4]  
copy_list[1] = 333  
print(copy_list)  
print(py_list) # [1, 2, 3, 4, 5] - remains same  
# Sliced Array is a VIEW  
np_arr = np.array([1, 2, 3, 4, 5])  
view_arr = np_arr[1:4] # [2, 3, 4]  
view_arr[1] = 333 
print(view_arr)  
print(np_arr) # [1, 2, 333, 4, 5] - changes  
# Creating a COPY for Array  
copy_arr = np_arr[1:4].copy() # [2, 3, 4]  
copy_arr[2] = 444 
print(copy_arr)  
print(np_arr) # [1, 2, 3, 4, 5] - remains same 