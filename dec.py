from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)


clf = DecisionTreeClassifier(random_state=42)
clf.fit(x_train, y_train)


y_pred = clf.predict(x_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Decision Tree classifier: {accuracy:.2f}")


plt.figure(figsize=(12, 8))
plot_tree(clf,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True)
plt.title("Decision Tree for Iris Dataset")
plt.show()


print("Enter the sample data:")
a = float(input("Enter sepal length in cm: "))
b = float(input("Enter sepal width in cm: "))
c = float(input("Enter petal length in cm: "))
d = float(input("Enter petal width in cm: "))

sample = [[a, b, c, d]]
pred = clf.predict(sample)
pred_v = [iris.target_names[p] for p in pred]
print("Predicted class:", pred_v[0])

