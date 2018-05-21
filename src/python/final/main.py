import arduino
import acceleration_classifier
import distance_classifier
import image_classifier
import cv2


def main():
    try:
        arduino_serial = arduino.Arduino("/dev/ttyACM0")
        aceleracion_clf = acceleration_classifier.create_model_from_file(
            "models/acceleration_clf2.pkl")

        distancia_clf = distance_classifier.create_model_from_file(
            "models/distance_clf.pkl")

        imagen_clf = image_classifier.ImageClassifier("models/image-clf.model", 1)

        print("[Info]", "Clasificadores listos")

        while True:

            sensor, data = arduino_serial.collect_data()
            if sensor == "aceleracion":
                prediction = aceleracion_clf.predict(data)

            elif sensor == "distancia":
                prediction = distancia_clf.predict(data)
            else:
                prediction = None
                continue

            # print(sensor, prediction)
            if prediction == "ANORMAL":
                print(sensor, " detectó falla en la vía")

            ret, image = imagen_clf.collect_data()
            if not ret:
                continue

            cv2.imshow("Camara", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            label = imagen_clf.predict(image)
            # print("Camara", label)

            if label == "Pothole":
                print("camara detectó falla en la vía")

    except KeyboardInterrupt:
        imagen_clf.release()
        print("Finalizado")


if __name__ == '__main__':
    main()
