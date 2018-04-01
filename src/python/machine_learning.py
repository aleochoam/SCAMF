from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib


class Classifier(object):
    def __init__(self):
        self.dt_class = tree.DecisionTreeClassifier(max_depth=3)

    def train_model(self, X):
        X_train, X_test, y_train, y_test = train_test_split(
            X.drop('label', axis=1), X['label'])

        self.dt_class.fit(X_train, y_train)

    def predric(self, X):
        return self.dt_class.predict(X)

    def export_model(self, name):
        joblib.dump(self.dt_class, '{}.pkl'.format(name))


def create_model_from_file(name):
    return joblib.load(name)
