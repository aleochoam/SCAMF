import serial
import numpy as np


def create_arduino():
    arduino_port = '/dev/ttyACM0'
    arduino = serial.Serial(arduino_port, timeout=1)
    return arduino


def create_file(filename):
    return open(filename, 'a')


def write_file(file, data):
    if type(data) == str:
        file.write(data)
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


def dato_individual():
    arduino = create_arduino()
    arduino.flush()
    file = create_file("pothole.data")

    input("Presione enter para escribir datos...")

    arduino.write(b'0')
    arduino.flush()
    print("Escritura realizada")
    data_in = arduino.readline()
    print("Datos recibidos")
    data_in = clean_data(data_in)
    write_file(file, data_in)
    file.close()
    arduino.close()


def escritura_constante():
    arduino = create_arduino()
    arduino.flush()
    file = create_file("not_pothole.data")

    input("Presione enter para escribir datos...")
    try:
        while True:
            arduino.write(b'0')
            arduino.flush()
            # print("Escritura realizada")
            data_in = arduino.readline()
            print("Datos recibidos")
            data_in = clean_data(data_in)
            write_file(file, data_in)

    except KeyboardInterrupt as e:
        print("Escritura finalizada")
        file.close()
        arduino.close()


if __name__ == '__main__':
    escritura_constante()
    # dato_individual()
