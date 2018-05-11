from machine_learning import create_model_from_file
from arduino import create_arduino
import numpy as np


def main():
    acc_clf = create_model_from_file("acceleration_clf2.pkl")
    arduino = create_arduino()

    arduino.flush()
    arduino.readline()
    while (True):    
        data_in = arduino.readline()
        data_in = data_in.decode("utf-8").strip()
        data_in = data_in.split(",")
        data_in = data_in[:3]
        data_in = [eval(x) for x in data_in]

        average = np.average(data_in)
        std = np.std(data_in)
        maximum = np.amax(data_in)
        minumum = np.amin(data_in)

        y_hat = acc_clf.predict([[average, std, maximum, maximum-minumum]])
        print([average, std], "->", y_hat)



if __name__ == '__main__':
    main()
