import serial
import numpy as np

def create_arduino():
    arduino_port = '/dev/ttyACM0'
    arduino = serial.Serial(arduino_port)
    return arduino


def create_file(filename):
    return open(filename, 'a')


def write_file(file, data):
    if type(data) == str:
        file.write(text)
        file.write("\n")
    elif type(data) == np.ndarray:
        file.write(" ".join(map(str, data)))
        file.write("\n")


def close_file(file):
    file.close()


def clean_data(data_in):
    data_size = 5
    try:
        data_in = data_in.decode("utf-8")
    except Exception:
        print("No se pudo leer los datos")
        exit()


    data_in = data_in.split(",")

    if len(data_in) != data_size + 1:
        print("No se pudo leer todos los datos")
        exit()
    data_in = data_in[:data_size]
    data_in = [eval(x) for x in data_in]
    data_in = np.array(data_in)
    return data_in

def main():
    arduino = create_arduino()
    file = create_file("output.data")
    input("Presione enter para escribir datos...")

    arduino.write(b"start")
    data_in = arduino.readline()
    data_in = clean_data(data_in)
    write_file(file, data_in)
    file.close()


if __name__ == '__main__':
    main()
