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

            # print(sensor, prediction)
            if prediction == "ANORMAL":
                print(sensor, " detectó falla en la vía")

            image = imagen_clf.collect_data()

            cv2.imshow("Camara", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            label = imagen_clf.predict(image)
            # print("Camara", label)

            if label == "Pothole":
                print("camara detectó falla en la vía")

            if prediction or label == "Pothole":
                arduino_serial.write(1)

    except KeyboardInterrupt:
        print("Finalizado")
    except Exception:
        pass
    finally:
        imagen_clf.release()


if __name__ == '__main__':
    main()
