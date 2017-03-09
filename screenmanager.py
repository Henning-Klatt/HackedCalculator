#!/usr/bin/env python
# coding: utf8
import time
import multiprocessing

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from status import Status
from keymanager import Keymanager
from display import disp

from fonts import font_hacked

#Dimensions: 240 x 320
class Manager:
    status = False
    def startScreen(self):
        global status
        print "Starting Screen Manager..."
        disp.clear()
        draw = disp.draw()
        #Y Links, X Links, Y Rechts, X Rechts
        draw.line((40, 0, 40, 319), fill=(255,255,255))
        draw_text(disp.buffer, "Henning's hacked calculator!", (45, 0), 90, font_hacked, fill=(255,255,255))
        disp.display()
        time.sleep(.1)
        status = multiprocessing.Process(target=Status().run, args = ())
        status.start()

    def showLogo(self):
        disp.clear()
        draw = disp.draw()
        draw.line((40, 0, 40, 319), fill=(255,255,255))
        draw_text(disp.buffer, "Henning's hacked calculator!", (45, 0), 90, font_hacked, fill=(255,255,255))
        disp.display()

    def stopScreen(self):
        global status
        status.terminate()
        self.showLogo()
        print "Quit Info Screen"

    def startKeymanager(self):
        print "Starting Key Manager..."
        self.keymanager = multiprocessing.Process(target=Keymanager().run, args = ())
        self.keymanager.start()


def draw_text(image, text, position, angle, font, fill=(255,255,255)):
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    rotated = textimage.rotate(angle, expand=1)
    image.paste(rotated, position, rotated)

def main():
    print "Main Funktion Call"


if __name__ == '__main__':
    main()
