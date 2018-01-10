# Helper functions for talking to the RGB strip via USB.
# Stanley H.I. Lio
from serial import Serial
import time


def dim(r,g,b,brightness):
    assert brightness >= 0 and brightness <= 1, 'brightness should be within [0,1]'
    r = [int(brightness*tmp) for tmp in r]
    g = [int(brightness*tmp) for tmp in g]
    b = [int(brightness*tmp) for tmp in b]
    return r,g,b


def write_led_strip(s,pixels):
    """pixels is a list of lists: [[r0,g0,b0],[r1.g1,b1],...]. All numbers are within [0,1.0]."""
    DELIMITER = 255
    # map [0,1.0] (float) to [0,254] (integer)
    tmp = [tuple(int(254*v) for v in pixel) for pixel in pixels]
    # flatten the list of lists
    # "[leaf for tree in forest for leaf in tree]" from SO
    # https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
    tmp = [v for c in tmp for v in c]
    assert DELIMITER not in tmp
    s.write(bytes(tmp))
    s.write(bytes([DELIMITER]))   # frame delimiter


class Strip(object):
    def __init__(self,length,port):
        self._disp_length = length
        self._s = Serial(port,115200*4,timeout=0.5)
        self._bar = [[0,0,0]]*self._disp_length
        self._commit()

    def blink(self,index,duration=0.1,dutycycle=0.5,color=None):
        assert duration >= 0
        self.set_bit(index,color)
        time.sleep(duration*dutycycle)
        self.clear_bit(index)
        time.sleep(duration*(1-dutycycle))

    def wink(self,index,duration=0.1,dutycycle=0.5):
        assert duration >= 0
        color = self._bar[index-1]
        self.clear_bit(index)
        time.sleep(duration*dutycycle)
        self.set_bit(index,color)
        time.sleep(duration*(1-dutycycle))

    def set_bit(self,index,color):
        """Color is a tuple (R,G,B) where R, G, and B are numbers within [0,1]. Index starts from zero."""
        assert index >= 0 and index <= self._disp_length - 1, 'index should be within [0,length-1]'
        self._bar[index] = color
        self._commit()

    def clear_bit(self,index):
        assert index >= 0 and index <= self._disp_length - 1, 'index should be within [0,length-1]'
        self.set_bit(index,[0,0,0])

    def set_all(self,pixels):
        assert len(pixels) >= len(self._bar)
        assert len(pixels[0]) == 3
        assert pixels[0][0] >= 0 and pixels[0][0] <= 1
        self._bar = list(pixels[0:self._disp_length])
        self._commit()

    def _commit(self):
        self._write(self._bar)

    def _write(self,pixels):
        write_led_strip(self._s,pixels)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._s.__exit__()

    def __del__(self):
        self._s.__del__()


if '__main__' == __name__:

    from itertools import cycle

    patterns = cycle([(0.005,0,0),(0,0.005,0),(0,0,0.005)])

    DISP_LENGTH = 8
    PORT = 'COM10'
    
    strip = Strip(DISP_LENGTH,PORT)
    for k in range(DISP_LENGTH):
        strip.set_bit(k,color=next(patterns))

    print('done.')
    
