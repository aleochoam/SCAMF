import serial


def create_arduino():
    arduino_port = '/dev/ttyACM0'
    arduino = serial.Serial(arduino_port)
    return arduino
