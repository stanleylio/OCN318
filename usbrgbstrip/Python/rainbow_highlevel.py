#!/usr/bin/python3
import time
from colorsys import hsv_to_rgb
from strip import Strip


DISP_LENGTH = 16
BRIGHTNESS = 0.05
SATURATION = 1.0
SPREAD = 1.0
STEP_DEGREE = 6


def rainbow(shift=0,spread=1,saturation=1,brightness=1):
    assert shift >= -1 and shift <= 1
    assert spread >= 0
    assert saturation >= 0 and saturation <= 1
    assert brightness >= 0 and brightness <= 1

    H = range(DISP_LENGTH)              # {0..DISP_LENGTH-1}
    H = [h/(DISP_LENGTH-1) for h in H]  # {0..1}
    H = [spread*h for h in H]           # {0..spread}
    H = [(h+shift)%1 for h in H]        # circular-shifted in the hue space

    return [hsv_to_rgb(h,saturation,brightness) for h in H]


if '__main__' == __name__:
    with Strip(DISP_LENGTH,'COM43') as strip:

        deg = 0

        while True:
            try:
                tmp = rainbow(shift=-deg/360.,spread=SPREAD,saturation=SATURATION,brightness=BRIGHTNESS)

                for k,v in enumerate(tmp):
                    strip.set_bit(k,v)
                    
                print('shift = {:5.1f} deg'.format(deg))

                deg += STEP_DEGREE
                deg %= 360

                #time.sleep(0.01)
            except KeyboardInterrupt:
                break
