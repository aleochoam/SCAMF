import pandas as pd
from machine_learning import Classifier
from arduino import create_arduino


def create_model():
    acceleration_model = Classifier()
    return acceleration_model


def collect_data(arduino):
    data_aceleracion = []
    print("Control + c para parar la recoleccion de datos")
    arduino.write(b's')
    arduino.readline()
    try:
        while True:
            data_in = arduino.readline()
            data_in = data_in.decode("utf-8").strip()

            if "Ac" in data_in:
                # los datos llegan en aceleración X Y Z
                data_in = data_in.replace("=", "")
                data_in = data_in.split("|")
                data_in = [x[5:] for x in data_in]
                data_in = [x.strip() for x in data_in]
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


def menu():
    # label = input("Ingrese tipo de datos que desea leer: \nCAMINANDO\nESTATICO")
    pass


def main():
    arduino = create_arduino()
    print("Empezando a leer datos")
    data_aceleracion = collect_data(arduino)

    # Etiquetar los datos
    data_aceleracion = label_data(data_aceleracion, "NORMAL")
    print(data_aceleracion)

    acceleration_classifier = create_model()

    acceleration_classifier.train_model(data_aceleracion)

    acceleration_classifier.export_model("acceleration_clf")
    arduino.close()


if __name__ == '__main__':
    main()
