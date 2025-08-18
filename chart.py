import numpy as np
import matplotlib.pyplot as plt
x=np.array(['Java','Python','Php','Javascript','C','C++'])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
colors=['cyan','yellow','red','orange','purple','blue']
plt.barh(x, y, color=colors)
plt.title('Horizontal chart')
plt.xlabel('Programming language')
plt.ylabel('Popularity')
plt.show()
