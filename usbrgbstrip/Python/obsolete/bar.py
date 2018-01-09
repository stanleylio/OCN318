from __future__ import division
from serial import Serial
from rainbow import write as write_led_bar
import time


class Bar(object):
    def __init__(self,length,port):
        self._disp_length = length
        self._s = Serial(port,115200,timeout=0.5)
        self._bar = [[0,0,0]]*self._disp_length
        self._commit()

    def blink(self,index,duration=0.1,dutycycle=0.5,color=None):
        assert duration >= 0
        assert index >= 1 and index <= self._disp_length
        self.set_bit(index,color)
        time.sleep(duration*dutycycle)
        self.clear_bit(index)
        time.sleep(duration*(1-dutycycle))

    def wink(self,index,duration=0.1,dutycycle=0.5):
        assert duration >= 0
        assert index >= 1 and index <= self._disp_length
        color = self._bar[index-1]
        self.clear_bit(index)
        time.sleep(duration*dutycycle)
        self.set_bit(index,color)
        time.sleep(duration*(1-dutycycle))

    def flickr(self):
        # if it was on, turn off and on; (wink)
        # if it was off, turn on and off. (blink)
        pass

    def set_bit(self,index,color=None):
        """1-based index"""
        assert index >= 1 and index <= self._disp_length
        if color is None:
            color = [0,0,0.1]
        self._bar[index-1] = color
        self._commit()

    def clear_bit(self,index):
        """1-based index"""
        assert index >= 1 and index <= self._disp_length
        self._bar[index-1] = [0,0,0]
        self._commit()

    def _commit(self):
        self._write(*zip(*self._bar))

    def _write(self,r,g,b):
        write_led_bar(self._s,r,g,b)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._s.close()

    #def __del__(self):
        #self._s.close()


if '__main__' == __name__:
    DISP_LENGTH = 8
    with Bar(DISP_LENGTH,'COM43') as bar:
        from random import random,randint
        from colorsys import hsv_to_rgb
        while True:
            #bar.blink(3,duration=0.1,repeat=5,dutycycle=0.1,color=[0,0,1])
            for i in range(randint(1,10)):
                bar.blink(randint(1,DISP_LENGTH),duration=random()/2,dutycycle=random(),\
                          color=hsv_to_rgb(random(),1,random()))

