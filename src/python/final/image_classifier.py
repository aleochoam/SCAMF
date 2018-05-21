from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import imutils
import cv2
import classifier


class ImageClassifier(classifier.Classifier):
    """docstring for ImageClassifier"""
    def __init__(self, model, camera_port):
        super(ImageClassifier, self).__init__(load_model(model))
        self.capture = cv2.VideoCapture(camera_port)

    def collect_data(self):
        return self.capture.read()

    def extract_features(self, image):
        # image = imutils.rotate(image, angle=180)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # pre-process the image for classification
        image = cv2.resize(image, (64, 64))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        return image

    def predict(self, image):
        image = self.extract_features(image)

        # classify the input image
        (not_pothole, pothole) = self.model.predict(image)[0]

        # build the label
        label = "Pothole" if pothole > not_pothole else "Not pothole"
        return label
        proba = pothole if pothole > not_pothole else not_pothole
        label = "{}: {:.2f}%".format(label, proba * 100)
        return label

    def label_image(self, orig, label):
        # draw the label on the image
        output = imutils.resize(orig, width=400)
        cv2.putText(output, label, (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # show the output image
        cv2.imshow("Output", output)

    def show_image(self, image):
        cv2.imshow("image", image)

    def release(self):
        self.capture.release()
        cv2.destroyAllWindows()
