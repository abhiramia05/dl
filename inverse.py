import numpy as np
a=int(input("enter the row  of matrix:"))
b=int(input("enter the coloum of matrix:"))
if a != b:
    print("Matrix must be square to compute its inverse.")
    exit()
matrix=[]
print("enter the elements")
for i in range(a):
	row=[]
	for j in range(b):
		element = int(input(f"Element [{i+1}, {j+1}]: "))
		row.append(element)
	matrix.append(row)
matrix_np=np.array(matrix)
inverse = np.linalg.inv(matrix_np)
print("\nOriginal Matrix:")
print(matrix_np)
print("inverse is")
print(inverse)
		

