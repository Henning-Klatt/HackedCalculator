#!/usr/bin/env python
# coding: utf8
import time
#import threading
from thread import start_new_thread

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import status
import keymanager

#Dimensions: 240 x 320
class Manager:
    @classmethod
    def startScreen(self, disp):
        disp.clear((0, 0, 0))
        draw = disp.draw()
        #Y Links, X Links, Y Rechts, X Rechts
        draw.line((40, 0, 40, 319), fill=(255,255,255))
        font_hacked = ImageFont.truetype('Fonts/hacked.ttf', 25)
        draw_text(disp.buffer, "Henning's hacked calculator!", (45, 0), 90, font_hacked, fill=(255,255,255))
        disp.display()
        time.sleep(2)
        print "1"
        #status_thread = threading.Thread(target=status.run(disp), args=())
        #status_thread.daemon = True
        start_new_thread(status.run,(disp))
        print "2"
        #status_thread.start()
        print "Statusscreen aktiviert!"

    def startKeymanager(self):
        keymanager_thread = threading.Thread(target=keymanager.run(), args=())
        #keymanager_thread.daemon = True
        keymanager_thread.start()
        print "Keymanager aktiviert!"


def draw_text(image, text, position, angle, font, fill=(255,255,255)):
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    rotated = textimage.rotate(angle, expand=1)
    image.paste(rotated, position, rotated)

def main():
    print "Main Funktion"


if __name__ == '__main__':
    main()
