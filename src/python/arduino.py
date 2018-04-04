import serial


def create_arduino():
    arduino_port = '/dev/ttyACM1'
    arduino = serial.Serial(arduino_port)
    return arduino
