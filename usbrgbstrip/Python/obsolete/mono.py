#!/usr/bin/python3
# 255 is reserved as frame delimiter!
#
from serial import Serial
import math,time
from colorsys import hsv_to_rgb


DISP_LENGTH = 16
DELIMITER = 255
MAX_BRIGHTNESS = 60    # [0,254].
SPREAD = 1.0


def rainbow(shift=0,spread=1,saturation=1,brightness=1):
    assert shift >= -1 and shift <= 1
    assert spread >= 0 and spread <= 1
    assert saturation >= 0 and saturation <= 1
    assert brightness >= 0 and brightness <= 1

    H = range(DISP_LENGTH)              # {0..DISP_LENGTH-1}
    H = [h/(DISP_LENGTH-1) for h in H]  # {0..1}
    H = [spread*h for h in H]           # {0..spread}
    H = [(h+shift)%1 for h in H]        # circular-shifted in the hue space
    #print(H)

    # why wouldn't this work?
    # the discontinuity should occur only at the two ends. this doesn't satisfy that.
    #H = deque([rr/(DISP_LENGTH-1) for rr in range(DISP_LENGTH)])
    #H = deque(H)
    #H.rotate(int(shift*DISP_LENGTH))
    
    return [hsv_to_rgb(h,saturation,brightness) for h in H]

def write(s,r,g,b):
    """r,g,b are list of length DISP_LENGTH with each element within [0,1]"""
    assert len(r) == len(g)
    assert len(r) == len(b)
    assert all([tmp <= 1 and tmp >= 0 for tmp in r])
    assert all([tmp <= 1 and tmp >= 0 for tmp in g])
    assert all([tmp <= 1 and tmp >= 0 for tmp in b])

    assert MAX_BRIGHTNESS != DELIMITER

    r = [int(MAX_BRIGHTNESS*tmp) for tmp in r]
    g = [int(MAX_BRIGHTNESS*tmp) for tmp in g]
    b = [int(MAX_BRIGHTNESS*tmp) for tmp in b]
    
    r = [DELIMITER - 1 if tmp == DELIMITER else tmp for tmp in r]
    g = [DELIMITER - 1 if tmp == DELIMITER else tmp for tmp in g]
    b = [DELIMITER - 1 if tmp == DELIMITER else tmp for tmp in b]
    assert DELIMITER not in r
    assert DELIMITER not in g
    assert DELIMITER not in b

    m = bytearray([v for c in zip(r,g,b) for v in c])   # just flattening the list of lists.
    s.write(m)
    s.write(bytes([DELIMITER]))   # frame delimiter


if '__main__' == __name__:

    with Serial('COM41',230400) as s:
        # hum... I was hoping to do this but it won't work:
#        write = lambda *args: write(s,*args)
# see https://stackoverflow.com/questions/3252228/python-why-is-functools-partial-necessary
        from functools import partial
        write = partial(write,s)
        
        deg = 0

        while True:
            try:
                r = [0]*DISP_LENGTH
                g = [0.1]*DISP_LENGTH
                b = [0.1]*DISP_LENGTH
                write(r,g,b)
                print('{:6.2f} deg'.format(deg))

                deg += 6
                deg %= 360
                time.sleep(0.01)
            except KeyboardInterrupt:
                break
