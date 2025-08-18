import matplotlib.pyplot as plt
x1=[1,2,3,4,5]
y1=[2,4,6,8,10]
x2=[1,2,3,4,5]
y2=[1,4,9,16,25]
plt.plot(x1,y1,label="Line 1:y=2x",color="red",marker="o")
plt.plot(x2,y2,label="Line 2:y=x**2",color='blue',marker='s')
plt.title("Two lines on same plot with legends")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

