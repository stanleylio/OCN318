import io, sys, time
from datetime import datetime
sys.path.append('/home/pi')
from serial import Serial
import matplotlib.pyplot as plt
plt.ion()

ser = Serial('/dev/ttyS0', 9600, timeout=0.2)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser), newline='\r')

x = []
y = []
while True:
    try:
        ser.flushInput()
        
        line = sio.readline()
        # Rxxxx
        d = int(line[1:5])
        ts = time.time()
        #dt = datetime.now()
        #print(ts, dt, d)

        x.append(ts)
        y.append(d)

        plt.clf()
        plt.plot(x, y, 'r')
        plt.grid(True)
        plt.pause(0.05)

        while len(x) > 100:
            x.pop(0)
        while len(y) > 100:
            y.pop(0)

    except KeyboardInterrupt:
        print('user interrupted')
        break
    except:
        print('weird stuff happened')
    


f.close()
ser.close()
plt.ioff()

