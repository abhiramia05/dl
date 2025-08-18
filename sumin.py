import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
total_sum=np.sum(arr)
coloumn_sum=np.sum(arr,axis=0)
row_sum=np.sum(arr,axis=1)
print("arr:")
print(arr)
print("sum is",total_sum)
print("coloumn sum is:",coloumn_sum)
print("row sum is:",row_sum)

