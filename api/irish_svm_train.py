from sklearn.externals import joblib
from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.svm import SVC

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

model = SVC(kernel='linear').fit(X_train, y_train)
y_pred = model.predict(X_test)
print(model.score(X_test, y_test.ravel()))
joblib.dump(model, 'model/iris_svm_model.pkl', compress=True)