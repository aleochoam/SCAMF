import cv2
import os


i = 0
capture = cv2.VideoCapture(1)
while True:
    ret, image = capture.read()

    if not ret:
        break

    name = str(i).zfill(10) + ".jpg"
    print(name)
    cv2.imwrite("fotos2/" + name, image)

    i = i+1

