#!/usr/bin/env python
# "sudo ./HypnoColors.py --led-rows=16 --led-cols=32 --led-parallel=1 --led-brightness=78 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2"
from samplebase import SampleBase
from time import sleep
from functions import *
from layer2 import *
from Sigil import *


class HypnoColors(SampleBase):
    def __init__(self, *args, **kwargs):
        super(HypnoColors, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix.CreateFrameCanvas()

        R = 255
        G = 0
        B = 0


        sleep(5)
        while True:
            for num in range(1, 6):
                MakeJapan(canvas, num, R, G, B)
                canvas = self.matrix.SwapOnVSync(canvas)
                sleep(.5217)
            break

        
        while True:
            MakeJapan(canvas, num, R, G, B)
            #MakeJapan(canvas, num, R, G, B)
            canvas = self.matrix.SwapOnVSync(canvas)
            sleep(.5217)

        
##        _red = 255
##        _green = 255
##        _blue = 255
##        fade = 0
##        
##        sleep(5)
##        
##        
##        #three!!
##        while True:
##            MakeRomanNumeralThree( canvas, 3, _red - fade, _green - fade, _blue - fade)
##            canvas = self.matrix.SwapOnVSync(canvas)
##            sleep(.005)
##            fade = fade + 2
##            if(fade >= 255):
##                MakeRomanNumeralThree( canvas, 3, 0x0, 0x0, 0x0)
##                canvas = self.matrix.SwapOnVSync(canvas)
##                break
##
##
##        _red = 255
##        _green = 255
##        _blue = 255
##        fade = 0
##        
##        #two!!!
##        while True:
##            MakeRomanNumeralTwo( canvas, 2, _red - fade, _green - fade, _blue - fade)
##            canvas = self.matrix.SwapOnVSync(canvas)
##            sleep(.005)
##            fade = fade + 2
##            if(fade >= 255):
##                MakeRomanNumeralTwo( canvas, 2, 0x0, 0x0, 0x0)
##                canvas = self.matrix.SwapOnVSync(canvas)
##                break
##
##                       
##        _red = 255
##        _green = 255
##        _blue = 255
##        fade = 0
##        
##        #one!!!
##        while True:
##            MakeRomanNumeralOne( canvas, 1, _red - fade, _green - fade, _blue - fade)
##            canvas = self.matrix.SwapOnVSync(canvas)
##            sleep(.005)
##            fade = fade + 2
##            if(fade >= 255):
##                MakeRomanNumeralOne( canvas, 1, 0x0, 0x0, 0x0)
##                canvas = self.matrix.SwapOnVSync(canvas)
##                break


            
if __name__ == "__main__":
    hypno_colors = HypnoColors()
    if (not hypno_colors.process()):
        hypno_colors.print_help()

