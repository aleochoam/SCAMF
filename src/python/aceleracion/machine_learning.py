from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn import svm


class Classifier(object):
    def __init__(self):
        # self.model = tree.DecisionTreeClassifier()
        self.model = svm.LinearSVC()

    def train_model(self, X):
        X_train, X_test, y_train, y_test = train_test_split(
            X.drop('label', axis=1), X['label'])

        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        print(
            "Entrenamiento finalizado, puntuación: ",
            accuracy_score(y_pred, y_test))

    def predric(self, X):
        return self.model.predict(X)

    def export_model(self, name):
        joblib.dump(self.model, '{}.pkl'.format(name))


def create_model_from_file(name):
    return joblib.load(name)
