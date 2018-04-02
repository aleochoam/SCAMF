from machine_learning import create_model_from_file
from arduino import create_arduino


def main():
    acc_clf = create_model_from_file("acceleration_clf.pkl")
    arduino = create_arduino()

    arduino.flush()
    arduino.readline()
    data_in = arduino.readline()
    data_in = data_in.decode("utf-8").strip()
    data_in = data_in.replace("=", "")
    data_in = data_in.split("|")
    data_in = [x[5:] for x in data_in]
    data_in = [x.strip() for x in data_in]
    data_in = [eval(x) for x in data_in]

    y_hat = acc_clf.predict([data_in])
    print(data_in, "->", y_hat)


if __name__ == '__main__':
    main()
