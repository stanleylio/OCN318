# Washed-out rainbow
#
# Stanley H.I. Lio
# hlio@hawaii.edu
# OCN318, S18

import time
from serial import Serial
from colorsys import hsv_to_rgb
from strip import write_led_strip


def rainbow(length,shift=0,spread=1,saturation=1,brightness=1):
    assert length > 0
    assert shift >= -1 and shift <= 1
    assert spread >= 0
    assert saturation >= 0 and saturation <= 1
    assert brightness >= 0 and brightness <= 1

    H = range(length)                   # {0..length-1}
    H = [h/(length-1) for h in H]       # {0..1}
    H = [spread*h for h in H]           # {0..spread}
    H = [(h+shift)%1 for h in H]        # circular-shifted in the hue space

    return [hsv_to_rgb(h,saturation,brightness) for h in H]


if '__main__' == __name__:

    DISP_LENGTH = 8
    PORT = '/dev/ttyACM0'

    BRIGHTNESS = 0.05
    SATURATION = 0.8
    SPREAD = 0.8
    STEP_DEGREE = 1

    with Serial(PORT,115200*4,timeout=0.5) as s:

        deg = 0
        while True:
            try:
                c = rainbow(DISP_LENGTH,shift=-deg/360.,spread=SPREAD,saturation=SATURATION,brightness=BRIGHTNESS)

                write_led_strip(s, c)
                
                print('shift = {:5.1f} deg'.format(deg))

                deg += STEP_DEGREE
                deg %= 360

                #time.sleep(0.001)
            except KeyboardInterrupt:
                break
