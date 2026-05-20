# Common Data Types  
import numpy as np
arr = np.array([1, 2, 3, 4, 5])  
arr2 = np.array([1.0, 2.0, 3.0])  
arr3 = np.array(["hello", "world", "prime", "ai/ml"])  
print(arr.dtype) # int64 
print(arr2.dtype) # float64  
print(arr3.dtype) # U  
# Complex Numbers  
arr1 = np.array([2 + 3j])  
arr2 = np.array([5 + 8j])  
print(arr1, arr1.dtype)  
print(arr1 + arr2)  
print(arr2 - arr1)  
# Objects  
arr = np.array (["hello", {1, 2, 3}, 3.14])  
print(arr, arr.dtype)   