#!/usr/bin/env python
# coding: utf8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

class Manager:
    @classmethod
    def startScreen(self, disp):
        disp.clear((0, 255, 0))


def main():
    print "Main Funktion"


if __name__ == '__main__':
    main()
