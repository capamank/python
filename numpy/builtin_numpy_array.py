import numpy as np
# Creating NumPy Arrays - from scratch  
arr1 = np.zeros((3, 4)) # 3x4 array of 0s  
print(arr1, arr1.shape)  
 
arr2 = np.ones((3, 3)) # 3x3 array of 1s  
print(arr2, arr2.shape)  
 
arr3 = np.full((2, 3), 5) # 2x3 array of 5s  
print(arr3, arr3.shape)  
 
arr4 = np.eye(3) # Identity matrix of 3x3  
print(arr4, arr4.shape)  
 
arr5 = np.arange(1, 20, 2) # Elements in range(1, 20)  
print(arr5, arr5.shape)  
 
arr6 = np.linspace(0, 10, 5) # Evenly spaced array  
print(arr6, arr6.shape)