from sklearn.externals import joblib
import classifier
import numpy as np


class AccelerationClassifier(classifier.Classifier):
    """SVM ML model for classify acceleration"""
    def __init__(self, model):
        super(AccelerationClassifier, self).__init__(model)

    def extract_features(self, data):
        average = np.average(data)
        std = np.std(data)
        maximum = np.amax(data)
        minumum = np.amin(data)

        return (average, std, maximum, maximum-minumum)


def create_model_from_file(name):
    return AccelerationClassifier(joblib.load(name))
