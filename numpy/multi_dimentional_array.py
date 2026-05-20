import numpy as np
#2d array
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr,np.sum(arr))

#sum of rows
row=np.sum(arr,axis=0)
print(row)
#sum of column
col=np.sum(arr,axis=1)
print(col)
#slicing a 2d array
print(arr[0:2,2:3])

#3d array
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(arr,arr.shape)
print(arr[0,1,1])
print(arr[:,0,:])
