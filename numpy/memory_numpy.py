import numpy as np
import sys  
size=100_000_000
python_list=list(range(size))
np_array=np.array(python_list)
print("Python list size:", sys.getsizeof(python_list) * len(python_list)) 
print("NumPy array size:",{np_array.nbytes}) 