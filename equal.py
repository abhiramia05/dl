import numpy as np
array1=np.array([1,2,3])
array2=np.array([1,2,3])
print(array1)
print(array2)
if np.array_equal(array1,array2):
	print("arrays are equal")
else:
	print("arrays are not equal")

