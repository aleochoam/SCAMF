import serial
import numpy as np

none_data = None, None


class Arduino(object):
    """Arduino python interface"""
    def __init__(self, serial_port):
        super(Arduino, self).__init__()
        self.serial_port = serial_port
        self.arduino = serial.Serial(self.serial_port)
        # self.arduino = open("./test/ejemplo.txt", "r")

    def collect_data(self):
        try:
            data_in = self.arduino.readline()

            if data_in == "":
                return none_data

            data_in = data_in.decode("utf-8")
            data_in = data_in.split(":")

            if len(data_in) != 2:
                return none_data

            sensor = data_in[0]
            data_in = data_in[1]
            data_in = data_in.split(",")

            if len(data_in) != 6:
                return

            data_in = data_in[:5]
            data_in = [eval(x) for x in data_in]
            data_in = np.array(data_in)

            return sensor, data_in

        except Exception:
            return none_data
