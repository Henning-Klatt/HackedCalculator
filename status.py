#!/usr/bin/env python
# coding: utf8

import threading
import time
from datetime import timedelta

class Status(object):
    def start(self, disp):
        print "Statusseite gestartet"
        thread = threading.Thread(target=run(disp), args=())
        thread.daemon = True
        thread.start()

def run(disp):
    while True:
        draw = disp.draw()
        font = ImageFont.truetype('Fonts/clean.ttf', 11)
        uptime = str(timedelta(seconds = float(open('/proc/uptime', 'r').readline().split()[0]))).rsplit('.', 1)[0]
        draw_text(disp.buffer, "Uptime: " + uptime, (20, 0), 90, font, fill=(255,255,255))
        disp.display()
        time.sleep(1)
