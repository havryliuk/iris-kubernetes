import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
print("Feature importances:", clf.feature_importances_)

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(clf, 'model.pkl')
