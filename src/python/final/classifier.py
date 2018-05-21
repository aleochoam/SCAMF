class Classifier(object):
    """base class for machine learning classifier"""
    def __init__(self, model):
        self.model = model

    def predict(self, X):
        features = self.extract_features(X)
        return self.model.predict([features])

    def extract_features(self, X):
        raise Exception("Not implemented")
