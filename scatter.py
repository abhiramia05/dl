import numpy as np
import matplotlib.pyplot as plt
Maths=np.array([88,92,80,89,100,80,60,100,80,34])
Science=np.array([35,79,79,48,100,88,32,45,20,30])
plt.scatter(Maths,Science)
plt.grid(True)
plt.title('Scatter Plot')
plt.xlabel('mathematics')
plt.ylabel('Science')
plt.show()
