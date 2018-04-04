import pandas as pd
import numpy as np
from machine_learning import Classifier
from arduino import create_arduino


def create_model():
    acceleration_model = Classifier()
    return acceleration_model


def collect_data(arduino):
    data = []
    arduino.flush()
    arduino.readline()
    print("Control + c para parar la recoleccion de datos")
    try:
        while True:
            data_in = arduino.readline()
            try:
                data_in = data_in.decode("utf-8")
            except Exception:
                continue
            # los datos llegan en aceleración X Y Z

            data_in = data_in.split(",")

            if len(data_in) != 4:
                continue
            data_in = data_in[:3]
            data_in = [eval(x) for x in data_in]
            data_in = np.array(data_in)

            # print(data_in)
            data.append(data_in)

    except KeyboardInterrupt:
        print("Finalizado tomar datos")
        return data


def extract_features(data_list):
    data_features = []
    for data_row in data_list:
        average = np.average(data_row)
        std = np.std(data_row)
        data_features.append([average, std])

    return data_features


# Toma una lista de datos y la convierte en un DataFrame con una etiqueta dada
def label_data(data, label):
    data = pd.DataFrame(data)
    data["label"] = label
    return data


def join_data(A, B):
    return pd.concat((A, B), axis=0).reset_index(drop=True)


def main():
    arduino = create_arduino()
    acceleration_classifier = create_model()

    print("Empezando a leer datos normales")
    aceleracion_normal = collect_data(arduino)
    features_normal = extract_features(aceleracion_normal)
    aceleracion_normal = label_data(features_normal, "NORMAL")

    input("Empezar a leer datos anormales")
    aceleracion_anormal = collect_data(arduino)
    features_anormal = extract_features(aceleracion_anormal)
    aceleracion_anormal = label_data(features_anormal, "ANORMAL")

    X = join_data(aceleracion_normal, aceleracion_anormal)
    print(X)

    acceleration_classifier.train_model(X)

    acceleration_classifier.export_model("acceleration_clf2")
    arduino.close()


if __name__ == '__main__':
    main()
