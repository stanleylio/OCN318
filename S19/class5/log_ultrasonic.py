# save ultrasonic sensor measurements to file
import io, sys, time
from datetime import datetime
sys.path.append('/home/pi')
from node.drivers.beep import beep
from serial import Serial


ser = Serial('/dev/ttyS0', 9600, timeout=0.2)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser), newline='\r')
f = open('filename.csv', 'a')

while True:
    try:
        line = sio.readline()
        # Rxxxx
        d = int(line[1:5])
        ts = time.time()
        dt = datetime.now()
    #    print(ts, dt, d)

        s = '{},{},{}\n'.format(ts, dt, d)
        print(s)

        f.write(s)
        f.flush()

    except KeyboardInterrupt:
        print('user interrupted')
        break
    except:
        print('weird stuff happened')
    


#    if d < 1000:
#        beep(on=0.01, off=0.01)
    

f.close()
ser.close()




