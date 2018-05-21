from sklearn.externals import joblib
import classifier
import numpy as np


class DistanceClassifier(classifier.Classifier):
    """SVM ML model for classify acceleration"""
    def __init__(self, model):
        super(DistanceClassifier, self).__init__(model)

    def extract_features(self, data):
        average = np.average(data)
        maximo = np.amax(data)
        minimo = np.amax(data)

        return (average, maximo, minimo, maximo - minimo)


def create_model_from_file(name):
    return DistanceClassifier(joblib.load(name))
