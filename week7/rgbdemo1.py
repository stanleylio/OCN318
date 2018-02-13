# Serial Port access - Turn off the first LED
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18
from serial import Serial

ser = Serial('COM20', 115200, timeout=1)
ser.write('rgb000000\n'.encode())
ser.close()

# But what if you have N LEDs? Don't want to use calculator and copy and paste N times.
