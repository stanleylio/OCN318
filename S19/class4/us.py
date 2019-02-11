from serial import Serial
from node.drivers.beep import beep
import io


with Serial('/dev/ttyS0', 9600, timeout=0.2) as _ser:
    sio = io.TextIOWrapper(io.BufferedRWPair(_ser, _ser), newline='\r')
    
    while True:
        #sio.flush()
        line = sio.readline()

        d = int(line[1:])
        print(d)

        if d < 1000:
            beep(on=0.01, off=0.01)
