from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument(
    "-m", "--model", required=True, help="path to trained model model")

args = vars(ap.parse_args())

# capture = cv2.VideoCapture("../nuevas-fotos/todo/video7.mp4")
# capture = cv2.VideoCapture("./examples/video1.mp4")
capture = cv2.VideoCapture(1)

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

while True:
    ret, image = capture.read()
    if not ret:
        break

    # load the image
    orig = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # pre-process the image for classification
    image = cv2.resize(image, (64, 64))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # classify the input image
    (not_pothole, pothole) = model.predict(image)[0]

    # build the label
    label = "Pothole" if pothole > not_pothole else "Not pothole"
    proba = pothole if pothole > not_pothole else not_pothole
    label = "{}: {:.2f}%".format(label, proba * 100)

    # draw the label on the image
    output = imutils.resize(orig, width=400)
    cv2.putText(
        output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # show the output image
    cv2.imshow("Output", output)
    if label == "Pothole":
        cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
