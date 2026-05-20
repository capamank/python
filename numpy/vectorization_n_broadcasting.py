import numpy as np

#vectiorization
arr = np.array([1, 2, 3, 4, 5])  
sq_arr = arr**2  # Square of all nums 
print(sq_arr)  
arr2 = np.array([6, 7, 8, 9, 10])  
print(arr + arr2)  # Sum of 2 arrays 

#broadcasting
# Broadcasting with a Scalar  
arr_mul10 = arr * 10 # Multiply by 10 to all nums  
print(arr_mul10)  
# Broadcasting with a Vector  
arr1D = np.array([1, 2, 3])  
arr2D = np.array([[1, 2, 3], [4, 5, 6]])  
print(arr1D + arr2D) 



#normalization 
arr=np.array=([[1,2,3],[1,2,3]])
mean=np.mean(arr)
std=np.std(arr)
print(np.mean(arr))
print(np.std(arr))
normalized=(arr-mean)/std
print(normalized)



