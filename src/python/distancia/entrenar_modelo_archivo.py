import pandas as pd
import numpy as np
from machine_learning import Classifier


def open_file(file_path):
    return open(file_path, "r")


def create_model():
    acceleration_model = Classifier()
    return acceleration_model


def collect_data(file):
    data = []
    data_in = file.readline()
    while data_in != "\n" and data_in != "":

        data_in = data_in.split(" ")

        data_in = data_in[:5]
        data_in = [eval(x) for x in data_in]
        data_in = np.array(data_in)

        data.append(data_in)
        data_in = file.readline()

    return data


def extract_features(data_list):
    data_features = []
    for data_row in data_list:
        average = np.average(data_row)
        std = np.std(data_row)
        maximum = np.amax(data_row)
        minimun = np.amin(data_row)
        data_features.append([average, std, maximum, minimun, maximum-minimun])
    return data_features


# Toma una lista de datos y la convierte en un DataFrame con una etiqueta dada
def label_data(data, label):
    data = pd.DataFrame(data)
    data["label"] = label
    return data


def join_data(A, B):
    return pd.concat((A, B), axis=0).reset_index(drop=True)


def main():
    file_not_pothole = open_file("./not_pothole.data")
    file_pothole = open_file("./pothole.data")

    acceleration_classifier = create_model()

    print("Empezando a leer datos normales")
    aceleracion_normal = collect_data(file_not_pothole)
    features_normal = extract_features(aceleracion_normal)
    aceleracion_normal = label_data(features_normal, "NORMAL")

    input("Empezar a leer datos anormales")
    aceleracion_anormal = collect_data(file_pothole)
    features_anormal = extract_features(aceleracion_anormal)
    aceleracion_anormal = label_data(features_anormal, "FALLA")

    X = join_data(aceleracion_normal, aceleracion_anormal)
    print(X)

    acceleration_classifier.train_model(X)

    acceleration_classifier.export_model("distance_from_file")
    file_not_pothole.close()
    file_pothole.close()


if __name__ == '__main__':
    main()
