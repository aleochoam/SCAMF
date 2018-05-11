import pandas as pd
from machine_learning import Classifier
from arduino import create_arduino


def create_model():
    acceleration_model = Classifier()
    return acceleration_model


def collect_data(arduino):
    data_aceleracion = []
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

            if "Ac" in data_in:
                # los datos llegan en aceleración X Y Z
                data_in = data_in.replace("=", "")
                data_in = data_in.split("|")
                if len(data_in) != 3:
                    continue

                data_in = [x[5:] for x in data_in]
                data_in = [x.strip() for x in data_in]
                data_in = [eval(x) for x in data_in]
                print(data_in)
                data_aceleracion.append(data_in)
            # else:
                # data_proximidad.append(data_in.replace("p", ""))
            # print(data_aceleracion, data_proximidad)

    except KeyboardInterrupt:
        print("Finalizado tomar datos")
        return data_aceleracion


# Toma una lista de datos y la convierte en un DataFrame con una etiqueta dada
def label_data(data, label):
    data = pd.DataFrame(data)
    data["label"] = label
    return data


def join_data(A, B):
    return pd.concat((A, B), axis=0).reset_index(drop=True)


def menu():
    # label = input("Ingrese tipo de datos que desea leer: \nCAMINANDO\nESTATICO")
    pass


def main():
    arduino = create_arduino()
    acceleration_classifier = create_model()

    print("Empezando a leer datos normales")
    aceleracion_normal = collect_data(arduino)
    aceleracion_normal = label_data(aceleracion_normal, "NORMAL")

    input("Empezar a leer datos anormales")
    aceleracion_anormal = collect_data(arduino)
    aceleracion_anormal = label_data(aceleracion_anormal, "ANORMAL")

    X = join_data(aceleracion_normal, aceleracion_anormal)
    print(X)

    acceleration_classifier.train_model(X)

    acceleration_classifier.export_model("acceleration_clf")
    arduino.close()


if __name__ == '__main__':
    main()
