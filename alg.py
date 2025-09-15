import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df=pd.read_csv('hw.csv')
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=c_knn.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter the sample data")
a=int(input("Enter Height in cm:"))
b=int(input("Enter Weight in cm:"))
pred_v=pd.DataFrame({"Height(cm)":[a],"Weight(cm)":[b]})
pred=c_knn.predict(pred_v)
print(pred)

