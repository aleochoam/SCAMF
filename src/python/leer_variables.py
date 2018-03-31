import serial
from machine_learning import Classifier
from sklearn import joblib


def create_arduino():
    arduino_port = '/dev/ttyUSB0'
    arduino = serial.Serial(arduino_port)
    return arduino


def create_model():
    acceleration_model = Classifier()
    return acceleration_model


def collect_data(arduino):
    data = []
    try:
        while True:
            data.append(arduino.read())
    except KeyboardInterrupt:
        print("Finalizado tomar datos")
        return data


def export_model(clf):
    joblib.dump(clf, 'trained_model.pkl')


def load_model(name):
    return joblib.load(name)


def main():
    arduino = create_arduino()
    print("Leyendo datos")
    data = collect_data(arduino)
    clf = create_model()
    clf.train_model(data)
    export_model(clf)
    print("Finalizado")


if __name__ == '__main__':
    main()
