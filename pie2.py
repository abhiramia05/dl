import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("pie.csv")
x=df["country"]
y=df["gold medal"]
plt.pie(y,labels=x)
plt.show()
