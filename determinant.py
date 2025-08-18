import numpy as np
a=int(input("enter the row  of matrix:"))
b=int(input("enter the coloum of matrix:"))
matrix=[]
print("enter the elements")
for i in range(a):
	row=[]
	for j in range(b):
		element = int(input(f"Element [{i+1}, {j+1}]: "))
		row.append(element)
	matrix.append(row)
matrix_np=np.array(matrix)
det=np.linalg.det(matrix_np)
print("determinant is")
print(det)
		

