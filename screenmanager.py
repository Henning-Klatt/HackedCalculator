#!/usr/bin/env python
# coding: utf8
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#Dimensions: 240 x 320
class Manager:
    @classmethod
    def startScreen(self, disp):
        disp.clear((0, 0, 0))
        draw = disp.draw()
        draw.line((0, 320), fill=(255,255,255))
        draw_text(disp.buffer, "Henning's hacked calculator!", (150, 120), 90, ImageFont.load_default(), fill=(255,255,255))
        disp.display()

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
