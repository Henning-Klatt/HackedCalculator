#!/usr/bin/env python
# coding: utf8
import time
#import threading
from threading import Thread

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
        print "Starting Screen Manager..."
        time.sleep(2)
        #status_thread = threading.Thread(target=status.run(disp), args=())
        #status_thread.daemon = True
        statusthread = Thread(target=status.run, args=(disp,))
        statusthread.start()
        print "Started Screen manager"

    def startKeymanager():
        keymanagerthread = Thread(target=keymanager.run, args=())
        #keymanager_thread.daemon = True
        keymanagerthread.start()
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
