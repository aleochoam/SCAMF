import serial
import pandas as pd
from machine_learning import Classifier


def create_arduino():
    arduino_port = '/dev/ttyACM0'
    arduino = serial.Serial(arduino_port)
    return arduino


def create_model():
    acceleration_model = Classifier()
    return acceleration_model


def collect_data(arduino):
    data_aceleracion = []
    data_proximidad = []
    print("Control + c para parar la recoleccion de datos")
    try:
        while True:
            data_in = arduino.readline()
            data_in = data_in.decode("utf-8").strip()

            if "a" in data_in:
                data_aceleracion.append(data_in.replace("a", ""))
            else:
                data_proximidad.append(data_in.replace("p", ""))
            print(data_aceleracion, data_proximidad)

    except KeyboardInterrupt:
        print("Finalizado tomar datos")
        return data_aceleracion, data_proximidad


# Toma una lista de datos y la convierte en un DataFrame con una etiqueta dada
def label_data(data, label):
    data = pd.DataFrame(data)
    data["label"] = label
    return data


def menu():
    label = input("Ingrese tipo de datos que desea leer: \n")


def main():
    arduino = create_arduino()
    print("Empezando a leer datos")
    data_aceleracion, data_proximidad = collect_data(arduino)

    # Etiquetar los datos
    data_aceleracion = label_data(data_aceleracion, "NORMAL")
    data_proximidad = label_data(data_proximidad, "NORMAL")

    acceleration_classifier = create_model()
    distance_classifier = create_model()

    acceleration_classifier.train_model(data_aceleracion)
    distance_classifier.train_model(data_proximidad)

    acceleration_classifier.export_model("aceleration_clf")
    distance_classifier.export_model("distance_clf")


if __name__ == '__main__':
    main()
