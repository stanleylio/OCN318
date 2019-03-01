import time
#from node.drivers.tsys01 import TSYS01
import random

class TSYS01:
    def read(self):
        return random.random()*25 + 10


sensor = TSYS01()
fout = open('lupin.csv', 'a')

while True:
    ts = time.time()
    temperature = sensor.read()
    
    print(ts, temperature)
    
    line = '{},{}\n'.format(ts, temperature)
    fout.write(line)
    fout.flush()
    
    time.sleep(1)

    
