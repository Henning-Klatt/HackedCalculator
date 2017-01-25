#!/usr/bin/env python
# coding: utf8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Manager:
    @classmethod
    def startScreen(self, disp):
        disp.clear((0, 0, 0))
        draw = disp.draw()
        draw.line((10, 170, 110, 230), fill=(255,255,255))
        disp.display()


def main():
    print "Main Funktion"


if __name__ == '__main__':
    main()
