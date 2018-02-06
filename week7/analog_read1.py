import time
from serial import Serial


with Serial('put your serial port here!', 115200, timeout=1) as ser:
    while True:
        ser.write('read_raw_a0\n'.encode())
        a0 = float(ser.readline().decode().strip())

        print(a0)
