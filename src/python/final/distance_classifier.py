from sklearn.externals import joblib
import classifier
import numpy as np


class DistanceClassifier(classifier.Classifier):
    """SVM ML model for classify acceleration"""
    def __init__(self, model):
        super(DistanceClassifier, self).__init__(model)

    def extract_features(self, data):
        average = np.average(data)
        std = np.std(data)
        maximum = np.amax(data)
        minimun = np.amin(data)

        return (average, std, maximum, minimun, maximum-minimun)


def create_model_from_file(name):
    return DistanceClassifier(joblib.load(name))
