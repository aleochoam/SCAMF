import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split


class Classifier(object):
    def __init__(self):
        self.tree = tree.DecisionTreeClassifier(max_depth=3)

    def importar_datos(self):
        static = np.random.randint(200, size=(100, 5))
        walking = np.random.randint(201, high=500, size=(100, 5))
        running = np.random.randint(501, high=1023, size=(100, 5))

        return (static, walking, running)

    def train_model(self, X):
        X_train, X_test, y_train, y_test = train_test_split(
            X.drop('label', axis=1), X['label'])

        self.dt_class.fit(X_train, y_train)

    def predric(self, X):
        return self.dt_class.predict(X)
